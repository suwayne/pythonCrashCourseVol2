"""
Make two files, cats.txt and dogs.txt. Store at least three names of cats in the 
first file and three names of dogs in the second file. Write a program that tries 
to read these files and print the contents of the file to the screen. Wrap your code 
in a try-except block to catch the FileNotFound error, and print a friendly message if a 
file is missing. Move one of the files to a different location on your system, and make sure 
the code in the except block executes properly.
"""

def print_words(filename):
    """Count the approximate number of words in a file."""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"Sorry, the file {filename} does not exist.")
        # pass #use pass if you want the file error to be silent
    else:
        # words = contents.split()
        # num_words = len(words)
        print(contents)

filename = 'ch10/cats.txt'
cats = print_words(filename) 
