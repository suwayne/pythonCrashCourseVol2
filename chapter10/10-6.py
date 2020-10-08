try:
    number_1 = int(input("Enter first number: "))
    number_2 = int(input("Enter second number: "))

except ValueError:
    print("Enter a number you cockroach!")
else:
    result = number_1 + number_2
    print(f"answer: {result}")
