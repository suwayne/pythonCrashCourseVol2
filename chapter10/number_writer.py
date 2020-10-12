import json

numbers = [2, 3, 5, 7, 8, 10]

filename = 'numbers.json'
with open(filename, 'w') as f:
    json.dump(numbers, f)
