
filename = 'ch10/alicee.txt'
try:
    with open(filename, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError: #this prints out your preset custom error mesage, and prevents the program from stopping
    print(f'Sorry, the file {filename} does not exist.')
#analyzing the text:

else:
    #count the number of words in the text:
    words = contents.split()
    num_words = len(words)
    print(f'the file {filename} is {num_words} words long.')
