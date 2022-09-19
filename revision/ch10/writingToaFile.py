"""this is an important lesson for cyber"""
"""this syntax will write 'i love programming' to a file called programming.txt"""

filename = 'programming.txt'
with open(filename, 'w') as file_object:
    file_object.write("I love programming.")