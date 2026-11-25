import json
from pathlib import Path

from jsonschema import validate, ValidationError

ROOT = Path(__file__).resolve().parent
STORYBOARD = ROOT / "storyboard.json"
SCHEMA = ROOT / "schema" / "storyboard.schema.json"


def load_json(path):
    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def validate_storyboard(storyboard, schema):
    validate(instance=storyboard, schema=schema)

    total_duration = sum(
        shot["duration"] for shot in storyboard["shots"]
    )

    if not 60 <= total_duration <= 90:
        raise ValueError(
            f"Film duration must be 60–90 seconds. Current: {total_duration}"
        )

    print("Storyboard validation successful!")
    print(f"Number of shots: {len(storyboard['shots'])}")
    print(f"Total duration: {total_duration} seconds")


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
            print("Narration:", shot["narration_am"])
            print("English subtitle:", shot["subtitle_en"])

    except (FileNotFoundError, json.JSONDecodeError, ValidationError, ValueError) as error:
        print(f"Pipeline error: {error}")
        raise SystemExit(1)


if __name__ == "__main__":
    main()
