#always look over and practice the snippets you find here

# #fizzbuzz challenge.

# for number in range(1, 101):
#     if number % 3 == 0 and number % 5 == 0:
#         print(f"{number} is a multiple of 3 and 5")
#     elif number % 5 == 0:
#         print(f"{number} is a multiple of 5")
#     elif number % 3 == 0:
#         print(f"{number} is a multiple of 3")

#     else:
#         print(number)
  

# length = input("input length: ")
# width = input("input width: ")

# area = int(length) * int(width)

# # print(f"the area is: {area}")
# print("the area is: " + str(area))


# length = int(input("input length: "))
# width = int(input("input width: "))

# area = length * width

# print(f"the area is: {area}")

# number = 2

# print(number + 1)

# alien_0 = {'color': 'green', 'speed': 'slow'}

# print(alien_0['points'])

# alien_0 = {'color': 'green', 'speed': 'slow'}

# point_value = alien_0.get('points', 'no point value assigned.') #this is what you do to return a message if the key you've requested
#                                                                 #does not exist.
# print(point_value)

# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python',
#     }

# # #this will print out the names of everyone who took the poll:
# # for name in favorite_languages.keys():
# #     print(name.title())


# friends = ['phil', 'sarah']

# #
# for name in favorite_languages.keys():  #loop through the f_l dictionary.
#     print(name.title())  #print each name or 'key' in the dictionary.

#     if name in friends:  #if the name is in the list called 'friends'
#         #store the value in the 'language varuable', you know we print values with 
#         #dictionary[key]. so you're storing the value in the variable 'language'.
#         language = favorite_languages[name].title()  
#         print(f"\t{name.title()}, I see you love {language}!")



# squares = []

# for value in range(1,11):
#     squares.append(value ** 2)
    

# print(squares)

# squares = [value ** 2 for value in range(1,11)]
# print(squares)


# count = 1 
# while count  <= 5:
#     print(count)
#     count += 1 

# unconfirmed_users = ['alice', 'brian', 'candace']   #1
# confirmed_users = []

# while unconfirmed_users:    #2
#     current_user = unconfirmed_users.pop()  #3

#     print(f"Verifying user: {current_user.title()}")
#     confirmed_users.append(current_user)   #4

# print("\nThe following users have been confirmed:")
# for confirmed_user in confirmed_users:
#     print(confirmed_user.title())


# responses = {}

# polling_active = True

# while polling_active:
#     name = input("\nwhat is your name?: ")
#     response = input("\nwhich mountain will you like to climb someday?: ")

#     responses[name] = response      #dictionariees key : value
#     repeat = input("would you like to let another person respond? (yes/no): ")

#     if repeat == 'no':
#         polling_active = False


# print("\nPolling Results:")
# for name, response in responses.items():
#     print(f"f{name} would like to climb {response}.")

"""
you're gonna spend the coming days reading chapter 7 again, so you can be awesome before you 
tackle function(ch8)
"""
