from random import choice

values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']

my_ticket = choice(values)

for i in range(0, len(values)):
    print(choice(values))
    if values[i] == my_ticket:
        print(f"It took {i+1} iterations to get the ticket {values[i]}")
        break 