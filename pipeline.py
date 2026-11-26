import json
from pathlib import Path

from jsonschema import Draft202012Validator, ValidationError

ROOT = Path(__file__).resolve().parent
STORYBOARD = ROOT / "storyboard.json"
SCHEMA = ROOT / "schema" / "storyboard.schema.json"


def load_json(path):
    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def validate_storyboard(storyboard, schema):
    Draft202012Validator.check_schema(schema)
    validator = Draft202012Validator(schema)

    errors = sorted(
        validator.iter_errors(storyboard),
        key=lambda error: list(error.path)
    )

    if errors:
        for error in errors:
            location = " -> ".join(str(part) for part in error.path)
            print(f"Validation error at {location or 'root'}: {error.message}")
        raise ValueError("Storyboard does not match the JSON schema.")

    total_duration = sum(
        shot["duration"] for shot in storyboard["shots"]
    )

    if not 60 <= total_duration <= 90:
        raise ValueError(
            f"Film duration must be 60–90 seconds. Current: {total_duration}"
        )

    print("Storyboard validation successful!")
    print(f"Number of shots: {len(storyboard['shots'])}")
    print(f"Planned shot duration: {total_duration:.2f} seconds")
    print(f"Target film duration: {storyboard['project']['target_duration_seconds']} seconds")


def main():
    try:
        storyboard = load_json(STORYBOARD)
        schema = load_json(SCHEMA)
        validate_storyboard(storyboard, schema)

        print("\nShot list:")
        for shot in storyboard["shots"]:
            print(f"\n{shot['id']} ({shot['duration']} seconds)")
            print("Visual:", shot["visual_prompt"])
            print("Motion:", shot["motion_prompt"])

            if "narration_am" in shot:
                print("Narration:", shot["narration_am"])

            if "subtitle_en" in shot:
                print("English subtitle:", shot["subtitle_en"])

    except (FileNotFoundError, json.JSONDecodeError, ValidationError, ValueError) as error:
        print(f"Pipeline error: {error}")
        raise SystemExit(1)


if __name__ == "__main__":
    main()
