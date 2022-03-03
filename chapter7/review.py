# prompt = "If you tell us who you are, we can personalize the messages you see."
# prompt += "\nWhat is your first name?: "

# name = input(prompt)
# print("\nhello, " + name + "!")

# height = input("How tall are you, in inches? ")
# height = int(height)

# if height >= 36:
#     print("\nYou're tall enough to ride!")
# else:
#     print("\nYou'll be able to ride when you're a little older.")

# roller coaster

# prompt = "if you tell us how old you are, we can personalize the message you see."
# prompt += "\nwhat is your first name? "

# name = input(prompt)

# print("hello, " + name)

# height = input("How tall are you, in inches? ")
# height = int(height)
# if height >= 36:
#     print("\nYou're tall enough to ride!")
# else:
#     print("\nYou'll be able to ride when you're a little older.")

# height = input("how tall are you")

# message = input("Tell me something, and I will repeat it back to you: ")
# print(message)

# number = input("enter a number, and i'll tell you if it's even or odd: ")
# number = int(number)

# if number % 2 == 0:
#     print("the number " + str(number) + " is even.")
# else:
#     print("the number " + str(number) + " is odd.")

# infinity loop
# count = 1

# while count <= 5:
#     print(count)
#     count += 1

# Start with users that need to be verified,
# and an empty list to hold confirmed users.
# unconfirmed_users = ['alice', 'brian', 'candace']
# confirmed_users = []

# Verify each user until there are no more unconfirmed users.
# Move each verified user into the list of confirmed users.

# while unconfirmed_users:
#     current_user = unconfirmed_users.pop()
#     print("Verifying user: " + current_user.title())
#     confirmed_users.append(current_user)

# Display all confirmed users.
# print("\nThe following users have been confirmed:")

# for confirmed_user in confirmed_users:
#     print(confirmed_user.title())

# removing all instances of specific values froma list
# pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
# print(pets)

# while 'cat' in pets:
#     pets.remove('cat')

# print(pets)

# filling a dictionary with user input

# responses = {}

# set a flag to indicate that polling is active.
# active = True
# while active:
# prompt for the person's name and response
# name = input("\nWhat is your name? ")
# response = input("Which mountain would you like to climb someday? ")

# store the response in the dictionary:
# responses[name] = response

# find out if anyone else is going to take the poll.
# repeat = input("would like to let another person respont (yes/no) ")
# if repeat == 'no':
#     active = False

# polling is complete. show the results.
# print("\n--- Poll Results ---")
# for name, response in responses.items():
#     print(name + " would you like to climb " + response + ".")
