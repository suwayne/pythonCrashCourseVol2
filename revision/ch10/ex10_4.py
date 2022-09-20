"""
Write a while loop that prompts users for their name. When they enter their name, 
print a greeting to the screen and add a line recording their visit in a file called 
guest_book.txt. Make sure each entry appears on a new line in the file.
"""

while True:
    name = input('what is your name?: ')
    print('welcome to the event, \nEnter quit to close this program')
    if name == 'quit':
        break
    else:

        filename = 'guest_book.txt'
        with open(filename, 'a') as file_object:
            file_object.write(f"{name}\n")

