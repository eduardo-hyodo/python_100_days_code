import requests

response =  requests.get(url="https://opentdb.com/api.php?amount=10&category=18&type=boolean")

question_data = []
for item in response.json()["results"]:
    question = { 
        "text": item["question"], 
        "answer": item["correct_answer"]  
    }
    question_data.append(question)


