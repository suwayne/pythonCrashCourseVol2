"""
Modify your except block in Exercise 10-8 to fail silently if either file is missing.
"""

def print_words(filename):
    """Count the approximate number of words in a file."""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"Sorry, the file {filename} does not exist.")
        # pass #use pass if you want the file error to be silent
        pass:
    else:
        # words = contents.split()
        # num_words = len(words)
        print(contents)

filename = 'ch10/cats.txt'
cats = print_words(filename) 

