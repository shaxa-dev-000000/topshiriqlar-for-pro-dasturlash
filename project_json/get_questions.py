import json

question = []
answers = []

with open('test.json', 'r') as f:
    data = json.load(f)
    for i in data:
        question.append(i["question"])
        answers.append(i["answers"])

def get_question():
    quiz = iter(question)
    for i in quiz:
        yield i

def get_answer():
    answer = iter(answers)
    for j in answer:
        yield j