
import os
import json
import base64
import requests

account_id = os.environ["CLOUDFLARE_ACCOUNT_ID"]
api_token = os.environ["CLOUDFLARE_API_TOKEN"]

url = f"https://api.cloudflare.com/client/v4/accounts/{account_id}/ai/run/@cf/black-forest-labs/flux-1-schnell"

headers = {
    "Authorization": f"Bearer {api_token}",
    "Content-Type": "application/json"
}
prompt = """
A photorealistic historical movie still of Saint Yared,
an elderly Ethiopian man, approximately 60 years old,
with a lighter warm-brown Ethiopian skin tone,
long shoulder-length naturally curly dark hair with
some grey strands, and a full long salt-and-pepper beard.
His face has natural wrinkles and realistic skin texture.

He wears traditional ancient Ethiopian cream robes
with subtle red, green and gold embroidery.

He is holding a VERY LARGE traditional Ethiopian begena
in both hands, a full-sized wooden ten-string lyre.
The begena is large and prominent in the foreground,
almost as tall as his upper body, with a beautifully
carved wooden frame and ten clearly visible strings.
His hands are naturally positioned while holding it.

He stands outside an ancient Ethiopian stone church.
Natural golden-hour sunlight, realistic human anatomy,
authentic historical atmosphere, cinematic documentary
photography, natural colors and textures.

Avoid illustration, painting, cartoon, CGI, fantasy,
plastic skin, glowing effects, exaggerated features,
distorted hands, and artificial-looking details.
No text, no watermark.
"""

response = requests.post(
    url,
    headers=headers,
    json={"prompt": prompt}
)

print("Status:", response.status_code)

if response.status_code == 200:
    result = response.json()

    if result.get("success") and result.get("result", {}).get("image"):
        image_data = base64.b64decode(result["result"]["image"])

        os.makedirs("keyframes", exist_ok=True)

        with open("keyframes/yared_final.jpg", "wb") as image:
            image.write(image_data)

        print("Final Saint Yared image saved successfully!")
    else:
        print(json.dumps(result, indent=2))
else:
    print(response.text)


data = {
    "prompt": "Cinematic historical artistic interpretation of Saint Yared, an Ethiopian sacred music scholar in the 6th century, standing in the ancient highlands of Ethiopia, traditional Aksumite-inspired clothing, ancient stone church in the distance, warm golden sunrise, respectful historical atmosphere, detailed realistic film still, no text"
}

response = requests.post(url, headers=headers, json=data)

print("Status:", response.status_code)

if response.status_code == 200:
    with open("keyframes/yared_test.png", "wb") as image:
        image.write(response.content)
    print("FLUX image generated successfully!")
else:
    print(response.text)