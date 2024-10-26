import customtkinter as ctk # pip install customtkinter
import tkinter
import os
import openai
from PIL import Image, ImageTk
import requests, io

def generate():
    openai.api_key = os.getenv("OPENAI_API_KEY")
    user_prompt = prompt_entry.get("0.0", tkinter.END)
    user_prompt += "in style: " + style_dropdown.get()

    response = openai.Image.create(
        prompt=user_prompt,
        n=int(number_slider.get()),
        size="512x512"
    )
    image_urls = []
    for i in range(len(response['data'])):
        image_urls.append(response['data'][i]['url'])
    print(image_urls)

    images = []
    for url in image_urls:
        response = requests.get(url)
        image = Image.open(io.BytesIO(response.content))
        photo_image = ImageTk.PhotoImage(image)
        images.append(photo_image)

    def update_image(index=0):
        canvas.image = images[index]
        canvas.create_image(0, 0, anchor="nw", image=images[index])
        index = (index + 1) % len(images)
        canvas.after(3000, update_image, index)

    update_image()