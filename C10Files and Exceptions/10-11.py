import json

question = input("what is your favourite number?: ")

with open('favorite_number.jsons', 'w') as f:
    json.dump(question, f)
    print(f"I know your favorite number is {question}.")
