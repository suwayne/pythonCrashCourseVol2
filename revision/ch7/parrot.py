prompt = "\nTell me something, and I will repeat it back to you:"  #1
prompt += "\nEnter 'quit' to end the program.\n: "


message = ""    #2
while message != "quit":    #3
    message = input(prompt)
    print(message)

