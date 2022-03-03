# try:
#     print(5/0)
# except ZeroDivisionError:
#     print("you cannot divide by zero")

print("Give me two numbers, and i'll divide them")
print("push 'q' to quit")

while True:
    first_number = input("\nEnter first number: ")
    if first_number == 'q':
        break
    second_number = input("\nEnter second number: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You cannot divide by zero.")
    else:
        print(f"Here's your answer: {answer}")
