"""
Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python. 
Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message
"""

def make_shirt(message_text='I love python', size='Large'):
    """prints a message on a shirt"""
    print(f"\nThis shirt is for body size {size}")
    print(f"Print message: {message_text}")

make_shirt()