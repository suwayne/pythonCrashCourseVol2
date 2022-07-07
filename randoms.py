#fizzbuzz challenge.

for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print(f"{number} is a multiple of 3 and 5")
    elif number % 5 == 0:
        print(f"{number} is a multiple of 5")
    elif number % 3 == 0:
        print(f"{number} is a multiple of 3")

    else:
        print(number)
  