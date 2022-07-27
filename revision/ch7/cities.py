"""
For example, consider a program that asks the user about places they’ve visited. 
We can stop the while loop in this program by calling break as soon as the user enters the 'quit' value:
"""

prompt = "\nPlease enter the name of a city you have visited"
prompt += "\n(Enter 'quit' when you are finished.): "

while True: 
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print(f"I'd love to go to {city.title()}!")

