import json

question = input("what is your favourite number?: ")

answer = 'question.json'
with open(answer, 'w') as f:
    json.dump(question, f)

# part 2
with open(answer) as f:
    question = json.load(f)
