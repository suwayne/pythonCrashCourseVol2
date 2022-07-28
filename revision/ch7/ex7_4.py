#ex 7_4.py: pizzatoppings.py
prompt = "\nEnter a series of pizza toppings. "
prompt += "\nType quit to exit: "

active = True

while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)

