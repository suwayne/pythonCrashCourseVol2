"""
One common problem when prompting for numerical input occurs when people provide 
text instead of numbers. When you try to convert the input to an int, youll get a 
ValueError. Write a program that prompts for two numbers. Add them together and print 
the result. Catch the ValueError if either input value is not a number, and print a friendly 
error message. Test your program by entering two numbers and then by entering some text 
instead of a number.
"""

first = input('enter the first number: ')
second = input('enter the second number: ')

try:
    addition = int(first + second)
except:
    print(f'sorry, you have entered a string, not an integer.')
else:
    print(f'the addition of {first} & {second} is {addition}')
