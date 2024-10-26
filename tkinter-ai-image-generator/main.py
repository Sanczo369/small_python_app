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