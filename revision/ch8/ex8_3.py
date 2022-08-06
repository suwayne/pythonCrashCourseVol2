"""

Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt. The 
function should print a sentence summarizing the size of the shirt and the message printed on it.Call the function once using 
positional arguments to make a shirt. Call the function a second time using keyword arguments."""

# def make_shirt(size, message_text):
#     """prints a message on a shirt"""
#     print(f"\nThis shirt is for body size {size}")
#     print(f"Print message: {message_text}")

# make_shirt(8, "don't hate the player hate the game")

#version 2:
def make_shirt(message_text, size=8):
    """prints a message on a shirt"""
    print(f"\nThis shirt is for body size {size}")
    print(f"Print message: {message_text}")

make_shirt("don't hate the player hate the game")

