import json

with open('favorite_number.json') as f:
    number = json.load(f)

print(f"I know your favorite number! It's {number}.")
