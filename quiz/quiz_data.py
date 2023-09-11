import requests

parameters = {
    "amount": 10,
    "type": "multiple"
}
response = requests.get(url="odnosnik do pytań", params=parameters)
question_data = response.json()["results"]

"""
Przykładowe Pytania

[
    {
        'category': 'Kategoria', 
        'type': 'Typ', 
        'difficulty': 'Trudność', 
        'question': 'Pytanie',
        'correct_answer': 'Prawidłowa Odpowiedź', 
        'incorrect_answers': [
            'nieprawidłowe_odpowiedzi 1', 
            'nieprawidłowe_odpowiedzi 2',
            'nieprawidłowe_odpowiedzi 3'
            ]
    }
]
"""