try:
    number_1 = input("Enter first number: ")

    number_2 = input("Enter second number: ")
except ValueError:
    print("Enter a number you cockroach!")
else:
    result = int(number_1) + int(number_2)
    print(f"answer: {result}")
