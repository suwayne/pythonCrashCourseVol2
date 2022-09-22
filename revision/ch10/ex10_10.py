import json

prompt = input("what is your name? ")
filename = 'invite_list.json' 

with open(filename, 'w') as f:
    json.dump(prompt, f)

