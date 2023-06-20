import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

user_prompt = input("Write your image prompt: ")

response = openai.Image.create(
    prompt = user_prompt,
    n = 1,
    size = "1024x1024"
)

image_url = response['data'][0]['url']
print(image_url)
