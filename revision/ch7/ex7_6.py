"""
Three Exits: Write different versions of either Exercise 7-4 or Exercise 7-5 that do each of the following at least once:
• Use a conditional test in the while statement to stop the loop.
• Use an active variable to control how long the loop runs.
• Use a break statement to exit the loop when the user enters a 'quit' value    
"""
prompt = "\nEnter a series of pizza toppings. "
prompt += "\nType quit to exit: "

active = True       #creating a variable 'active' and assingin it the boolean 'True'

while active:       #using the variable 'active' to control how long the loop runs.
    message = input(prompt) 

    if message == 'quit' or 'end':
        break       #using a break statement to end the loop when a user enters 'quit' or 'end'.
    else:
        print(message)

