"""this is an important lesson for cyber"""
"""this syntax will write 'i love programming' to a file called programming.txt"""

filename = 'programming.txt'
with open(filename, 'w') as file_object:
    file_object.write("I love programming.")

#you can write multiple lines too
    file_object.write("Yes, I really love the python way of coding")
    file_object.write("I will be using this newly acquired skill to automate my daily tasks.")

    