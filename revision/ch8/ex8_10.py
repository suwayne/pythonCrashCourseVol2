"""
Start with a copy of your program from Exercise 8-9. Write a function called 
send_messages() that prints each text message and moves each message to a new 
list called sent_messages as its printed. After calling the function, print 
both of your lists to make sure the messages were moved correctly.
"""

def show_message(messages):
    """print out each message"""
    for message in messages:
        print(message)
 

def send_messages(messages, sent_messages):
    while messages: 
        current_message = messages.pop()
        print(current_message)
        sent_messages.append(current_message)


short_messages = ['welcome to the team', 'happy monday', 'its good to have you here',]
sent_messages = []

