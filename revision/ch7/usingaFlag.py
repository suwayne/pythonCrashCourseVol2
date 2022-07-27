#using a flag
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

active = True       #we set 'active' to true, so that the program starts in an active state
while active:
    message = input(prompt)

    if message == "quit":
        active = False
    else: 
        print(message)
    


