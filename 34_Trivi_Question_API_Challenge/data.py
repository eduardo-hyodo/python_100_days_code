import requests

parameters = {
    "amount": 10,
    "category": 18,
    "type": "boolean"
}

response =  requests.get(url="https://opentdb.com/api.php", params=parameters)

question_data = []
for item in response.json()["results"]:
    question = { 
        "text": item["question"], 
        "answer": item["correct_answer"]  
    }
    question_data.append(question)


