import os
import openai  # pip install openai
import customtkinter as ctk  # pip install customtkinter


def generate():
    prompt = "Please generate 10 ideas for coding projects. "
    language = language_dropdown.get()
    prompt += "The programming language is " + language + ". "
    difficulty = difficulty_value.get()
    prompt += "The difficulty is " + difficulty + ". "

    if checkbox1.get():
        prompt += "The project should include a database. "
    if checkbox2.get():
        prompt += "The project should include an API."

    print(prompt)

    openai.api_key = os.getenv("OPENAI_API_KEY")
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    answer = response.choices[0].message.content
    print(answer)
    result.insert("0.0", answer)
