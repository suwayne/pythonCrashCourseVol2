from random import choice

possibilities = ['a', 'c', 'b', 'd', 'f', 10, 8, 3, 2, 5, 6, 4, 7, 9, 1]

winning_ticket = []

print("let's see what the winning ticket is:")

# only add the pulled item to the winning ticket if it hasn't
# been pulled.
while len(winning_ticket) < 4:
    pulled_item = choice(possibilities)

    if pulled_item not in winning_ticket:
        print(f"We pulled a {pulled_item}")
        winning_ticket.append(pulled_item)
        print(f"The final winning ticket is: {winning_ticket}")
