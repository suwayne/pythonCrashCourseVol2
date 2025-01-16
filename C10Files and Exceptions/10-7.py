print("Enter 'q' at any time to quit.\n")

while True:
    try:
        number_1 = input("Enter first number: ")
        if number_1 == 'q':
            break
        number_1 = int(number_1)

        number_2 = input("Enter second number: ")
        if number_2 == 'q':
            break
        number_2 = int(number_2)

    except ValueError:

        print("Enter a number grasshoppper!")

    else:
        result = number_1 + number_2
        print(f"answer: {result}")
