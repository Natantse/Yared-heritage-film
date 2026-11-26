import os
from google import genai
from google.genai import types

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

narration = open("narration_am.txt", encoding="utf-8").read()

response = client.models.generate_content(
    model="gemini-3.8-flash-tts",
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

audio = response.candidates[0].content.parts[0].inline_data

os.makedirs("narration", exist_ok=True)

with open("narration/narration_am.wav", "wb") as f:
    f.write(audio.data)

print("Narration generated successfully!")