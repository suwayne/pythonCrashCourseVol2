import os

# filename = '/Users/osasumwenogbebor/Documents/dev/pythonCrashCourseVol2/chapter10/alice.txt'
filename = 'alice.txt'

try:
    with open(filename, encoding='UTF-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry the file {filename} does not exist.")

else:
    # count the approximate number of words in the file.
    words = contents.split()
    num_words = len(words)
    print(f"The file {filename} has about {num_words} words.")
    print(f"This script is being run from {os.getcwd()}")
