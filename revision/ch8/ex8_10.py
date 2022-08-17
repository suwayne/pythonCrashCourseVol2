"""
Start with a copy of your program from Exercise 8-9. Write a function called 
send_messages() that prints each text message and moves each message to a new 
list called sent_messages as its printed. After calling the function, print 
both of your lists to make sure the messages were moved correctly.
"""

#this function prints out all the messages in a list
def show_message(messages):
    """print out each message"""
    for message in messages:
        print(message)
 
#this function takes messages from a populated list prints it out and stores it in the empty list.
#parameters; message and sent_messages are place holders for the populated list and the empty list.
def send_messages(messages, sent_messages):
    while messages: 
        current_message = messages.pop()
        print(current_message)
        sent_messages.append(current_message)


short_messages = ['welcome to the team', 'happy monday', 'its good to have you here',]
sent_messages = []

show_message(short_messages)
send_messages(short_messages, sent_messages)

print(short_messages)
print(sent_messages)
