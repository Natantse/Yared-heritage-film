import os
from google import genai
from google.genai import types

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

with open("narration_am.txt", encoding="utf-8") as f:
    narration = f.read()

response = client.models.generate_content(
    model="gemini-2.5-flash-preview-tts",
    contents=narration,
    config=types.GenerateContentConfig(
        response_modalities=["AUDIO"],
        speech_config=types.SpeechConfig(
            voice_config=types.VoiceConfig(
                prebuilt_voice_config=types.PrebuiltVoiceConfig(
                    voice_name="Kore"
                )
            )
        )
    )
)

for part in response.parts:
    if part.inline_data:
        os.makedirs("narration", exist_ok=True)
        with open("narration/narration_am.wav", "wb") as f:
            f.write(part.inline_data.data)
        print("Narration generated successfully!")
        break
else:
    print("No audio was returned.")
