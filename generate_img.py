from voice_translator import listen, translate
import requests
import urllib.parse
import os

# Listen to user's speech
text = listen()

if text is None:
    print("No speech detected.")
    exit()

print("Original:", text)

# Translate to English
prompt = translate(text)

print("Translated:", prompt)

# Encode prompt for URL
encoded_prompt = urllib.parse.quote(prompt)

# Pollinations AI Image API
url = f"https://image.pollinations.ai/prompt/{encoded_prompt}"

print("Generating image...")

response = requests.get(url)

if response.status_code == 200:
    with open("generated_image.png", "wb") as f:
        f.write(response.content)

    print("Image generated successfully!")

    # Open image automatically
    os.startfile("generated_image.png")

else:
    print("Failed to generate image.")
    print(response.status_code)