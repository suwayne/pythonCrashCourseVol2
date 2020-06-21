alien_0 = {'color': 'green', 'points': 5}

# this is how you add values to a dictionary
alien_0['x_cordinate'] = 40
alien_0['model'] = 'sony'

# print(alien_0['color'])
# print(alien_0['points'])

print(alien_0['x_cordinate'])


# responses = {}
# # set a flag to indicate poling is active.
# polling_active = True

# while polling_active:
#     # prompt for name and response
#     name = input("\nWhat is your name?: ")
#     response = input("what mountain will you like to climb?: ")

#     # store the response in the dictionary
#     responses[name] = response

#     # Find out if anyone else is going to take the poll.
#     repeat = input("would you like to let another person respond? (yes/no)")
#     if repeat == 'no':
#         polling_active = False

# print("\n-- Poll Results ---")
# for name, response in responses.items():
#     print(f"{name} {response}.")
