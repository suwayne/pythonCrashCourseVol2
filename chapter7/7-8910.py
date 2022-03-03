# #deli and pastrimi
# sandwich_orders = ['pastrimi', 'chicken', 'tuna',
#                    'pastrimi', 'fish', 'vegetable', 'pastrimi']
# finished_sandwiches = []

# print()
# print("Deli has run out of pastrimi sandwich.")
# while 'pastrimi' in sandwich_orders:
#     sandwich_orders.remove('pastrimi')

# while sandwich_orders:
#     current_order = sandwich_orders.pop()
#     print("\tI made your " + current_order + " sandwich.")
#     finished_sandwiches.append(current_order)

# # display all sandwiches prepared
# print("\n---Here's a list of all sandwiches prepared---\n")
# for i, sandwich in enumerate(finished_sandwiches, 1):
#     print(i, '. ' + sandwich, sep='', end='\n')

# dream vacation
vacation_spot = {}

# set flag for polling active
active = True

while active:
    # prompt for the persons name and response
    name = input("\nwhat is your name? ")
    question = input("what location would you like to visit? ")

    # store the response in a dictionary
    vacation_spot[name] = question

    # find out if someone else wants to take the poll
    repeat = input("would anyone else like to respond? (yes/no) ")
    if repeat == 'no':
        active = False

        # polling is complete. show the results
        print("\n--results--")
        for name, question in vacation_spot.items():
            print(name + " would like to visit " + question + ".")
