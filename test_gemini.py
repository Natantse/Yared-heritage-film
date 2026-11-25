import os
from google import genai

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

response = client.models.generate_content(
model="gemini-3.6-flash",
    contents="Write a short introduction in Amharic about Saint Yared and his contribution to Ethiopian sacred music. Make it suitable for an international audience."
)

print(response.text)