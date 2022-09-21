"""
Wrap your code from Exercise 10-6 in a while loop so the user can continue entering 
numbers even if they make a mistake and enter text instead of a number.
"""

while True:
    first = input('enter the first number: ')
    second = input('enter the second number: ')

    try:
        addition = int(first) + int(second)

    except ValueError:
        print(f'sorry, you have entered a string, not an integer.')
    else:
        print(f'the addition of {first} & {second} is {addition}')
