"""
Make a list containing a series of short text messages. Pass the list to a 
function called show_messages(), which prints each text message.
"""

def show_message(messages):
    """print out each message"""
    for message in messages:
        print(message)
    
 
short_messages = [
    'welcome to the team', 'happy monday', 'its good to have you here', 'welcome to the group',
    'aloha', 'koyo o', 'thanks for stopping by',
    ]

show_message(short_messages)
