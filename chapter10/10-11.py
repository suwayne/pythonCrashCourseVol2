import json

question = input("what is your favourite number?: ")

with open(answer, 'w') as f:
    json.dump(question, f)
    print(f"I know your favorite number is {question}.")
