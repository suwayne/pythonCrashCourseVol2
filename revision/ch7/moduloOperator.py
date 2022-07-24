"""
the % 'modulo' operator tells you how much is left after you divide two numbers,
it's also a good way to determine whether a number is even or odd.
"""
number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
    print(f"The value: {number} you entered is even.")
else:
    print(f"The value: {number} you entered is odd.")


