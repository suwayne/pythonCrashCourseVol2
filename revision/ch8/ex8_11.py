"""
Start with your work from Exercise 8-10. Call the function send_messages() with a copy of the list 
of messages. After calling the function, print both of your lists to show that the original list has retained its messages.
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


send_messages(short_messages[:], sent_messages)

print(short_messages)
print(sent_messages)
