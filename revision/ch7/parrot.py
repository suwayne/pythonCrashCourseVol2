prompt = "\nTell me something, and I will repeat it back to you:" 
prompt += "\nEnter 'quit' to end the program.\n: "

message = ""
while message.lower() != 'quit':
    message = input(prompt)
    print(message)

