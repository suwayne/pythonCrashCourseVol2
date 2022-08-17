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
  

# length = (" length: ")
# width = (" width: ")

# area = int(length) * int(width)

# # print(f"the area is: {area}")
# print("the area is: " + str(area))


# length = int((" length: "))
# width = int((" width: "))

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
#     name = ("\nwhat is your name?: ")
#     response = ("\nwhich mountain will you like to climb someday?: ")

#     responses[name] = response      #dictionariees key : value
#     repeat = ("would you like to let another person respond? (yes/no): ")

#     if repeat == 'no':
#         polling_active = False


# print("\nPolling Results:")
# for name, response in responses.items():
#     print(f"f{name} would like to climb {response}.")

"""
you're gonna spend the coming days reading chapter 7 again, so you can be awesome before you 
tackle function(ch8) :)
"""
# message = ("tell me something, and i'll repeat it back to you: ")
# # print(message)

# name = ("what is your name?: ")
# print(f"hello {name}!, you are welcome to the platform")

# prompt = "If you tell us who you are, we can personalize the message you see"
# prompt += "\nWhat's your first name?: "

# name = (prompt)

# age = ("how old are you?: ")
# age = int(age)

# print(2 + age)

#rollercoaster.py example:

# height = ("how old are you in inches?: ")
# height = int(height)

# if height >= 48:
#     print("\nyou are tall enough to ride")
# else:
#     print("\nyou'll be old enough to ride when you're a bit older")

#even_or_odd.py
# number = ("enter a number, i'll tell you if it's odd or even: ")
# number = int(number)

# if number % 2 == 0:
#     print(f"{number} is even")
# else:
#     print(f"{number} is odd")

#ex7_1 rental car:
"""
Write a program that asks the user what kind of rental car they would like. Print a message about that car, such as “Let me see if I can find you
"""
# car = ("what kind of rental car would you like?: ")
# print(f"let me see if i can find you a {car}.")

#ex7_2 restaurant seating: 
"""
Write a program that asks the user how many people are in their dinner group. If the answer is more than eight, print a message saying theyll 
have to wait for a table. Otherwise, report that their table is ready.
"""
# number = ("how many people are you bringing along?: ")
# number = int(number)
# if number > 8:
#     print(f"your {number} requires you have to wait a little.")
# else:
#     print(f"your group size of {number} gives you immediate access to a table.")

#ex7_3 multiples of ten:
"""
Ask the user for a number, and then report whether the number is a multiple of 10 or not.
"""
# number = ("enter a number: ")
# number = int(number)

# if number % 10 == 0:        #the comparision operator
#     print(f"this {number} is a multiple of 10")
# else:
#     print(f"this {number} is not a multiple of 10")

# counting.py
# current_number = 1
# while current_number <= 5:
#     print(current_number)
#     current_number += 1

#parrot.py
# prompt = "\ntell me something and i will repeat it back to you"
# prompt += "\nenter quit to end the program: "
# message = ""

# while message != "quit":
#     message = (prompt)

#blue highligh is for revision
""""""
# prompt = "\nTell me something, and I will repeat it back to you."
# prompt += "\nEnter 'quit' to end the program: "
# active = True

# while active:
#     message = (prompt) 

#     if message == 'quit':
#         active = False
#     else:
#         print(message)



# prompt = "\nPlease enter the name of a city you have visited:"
# prompt += "\n(Enter 'quit' when you are finished.) "

# while True:
#     city = (prompt)
#     if city == 'quit':
#         break
#     else:
#         print(f"I'd love to go to {city.title()}!")


# current_number = 0
# while current_number < 10: 
#     current_number += 1
#     if current_number % 2 == 0:
#            continue     #if the condition above isn't met; return to the begining of the loop :)

#     print(current_number)

# x= 1
# while x <= 5:
#     print(x)
#     x += 1

#ex: pizza toppings
# prompt = "enter a pizza topping."
# prompt += "\n(Enter 'quit' to end the program): "

# while True:
#     message = (prompt)
#     if message == 'quit': 
#         break
#     else: 
#         print(prompt)
    
# ex: movie tickets
# prompt = "what is your age?"
# prompt += "enter quit to exit the program: "

# while True:
#     poll = (prompt)
#     if poll == 'quit':
#         break
    
#     poll = int(poll)
#     if poll <= 3:
#         print("your movie ticket is free")
#     elif poll <= 12:
#         print("your ticket will cost $10")
#     else:
#         print("your ticket is $15")

# ex: three exits
# prompt = "what is your age?"
# prompt += "\nenter quit to exit the program: "
# active = True

# while active:
#     poll = (prompt)
#     if poll == 'quit':
#         break
    
#     poll = int(poll)
#     if poll <= 3:
#         print("your movie ticket is free")
#     elif poll <= 12:
#         print("your ticket will cost $10")
#     else:
#         print("your ticket is $15")

# pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat'] 
# print("\noriginal list of pets below:")
# print(pets)

# while 'cat' in pets:
#     pets.remove('cat')
# print(pets)

# responses = {}
# # Set a flag to indicate that polling is active.
# polling_active = True
# while polling_active:
#     # Prompt for the person's name and response.
#     name = ("\nWhat is your name? ")       #this is the key
#     response = ("Which mountain would you like to climb someday? ")        #this is the value
#     # Store the response in the dictionary.
#     responses[name] = response
#     # Find out if anyone else is going to take the poll.
#     repeat = ("Would you like to let another person respond? (yes/ no) ")
#     if repeat == 'no':
#         polling_active = False
# # Polling is complete. Show the results.
# print("\n--- Poll Results ---")
# for name, response in responses.items():
#     print(f"{name} would like to climb {response}.")

"""
Make a list called sandwich_orders and fill it with the names of vari- ous sandwiches. Then make 
an empty list called finished_sandwiches. Loop through the list of sandwich orders and print a 
message for each order, such as I made your tuna sandwich. As each sandwich is made, move it to the
 list of finished sandwiches. After all the sandwiches have been made, print a message listing 
 each sandwich that was made.
"""
# sandwich_orders = ['chicken', 'beef', 'tuna', 'egg', 'turkey', 'vegetable']
# finished_sandwiches = []

# for complete in sandwich_orders:
#     print(f"I made your {complete} sandwich")
    
# while sandwich_orders:
#     made_sandwich = sandwich_orders.pop()
#     finished_sandwiches.append(made_sandwich)

# print(f"\nfinished sandwiches:")
# for finished in finished_sandwiches:
#     print(finished)

# ex:no pastrimi
"""
Using the list sandwich_orders from Exercise 7-8, make sure the sandwich 'pastrami' appears in the 
list at least three times. Add code near the beginning of your program to print a message saying the
 deli has run out of pastrami, and then use a while loop to remove all occurrences of 'pastrami' 
 from sandwich_orders. Make sure no pastrami sandwiches end up in finished_sandwiches.
"""
# sandwich_orders = ['chicken', 'beef', 'tuna', 'egg', 'turkey', 'vegetable']
# finished_sandwiches = []

# for complete in sandwich_orders:
#     print(f"I made your {complete} sandwich")
    
# while sandwich_orders:
#     made_sandwich = sandwich_orders.pop()
#     finished_sandwiches.append(made_sandwich)

# print(f"\nfinished sandwiches:")
# for finished in finished_sandwiches:
#     print(finished)

#ex dream vacation:
"""
Dream Vacation: Write a program that polls users about their dream vacation. Write a prompt 
similar to If you could visit one place in the world, where would you go? Include a block of code 
that prints the results of the poll.
In addition if nobody enters any poll before it quits, print "there were no participants"
"""

# answers = []
# poll = "If you could visit one place in the world where would you go?: "
# poll += "\nEnter 'quit' to end the program: "

# while True:
#     message = (poll)
#     answers.append(message)
#     if message == 'quit':
#         break

# print(answers)
    

"""
A function that accepts a first and last name and returns it as a fully formatted name.
"""

# def full_name(first_name, last_name):
#     person = {'first':first_name, 'last':last_name}     #this is how you accept the first and last names
#     return person       #here you return the variable where the first and last name's are stored

# musician = full_name('burna', 'boy')        #here we create a new object (musician) to store the first and last name
# print(musician)                             #here we print out the output in dictionary form, as it should be, based on the function we created


#come and practice ch8 here, thanks :)
# def make_album(artist, title):
#     """Build a dictionary containing information about an album."""
#     album_dict = {
#         'artist': artist.title(),
#         'title': title.title(),
#         }
#     return album_dict

# album = make_album('metallica', 'ride the lightning')
# print(album)

# album = make_album('beethoven', 'ninth symphony')
# print(album)

# album = make_album('willie nelson', 'red-headed stranger')
# print(album)


# def make_album(artist_name, album_title):
#     album_dict = {
#         'artist': artist_name.title(),
#         'title': album_title.title(),
#     }
#     return album_dict

# def make_album(artist, title, tracks=0):
#     """Build a dictionary containing information about an album."""
#     album_dict = {
#         'artist': artist.title(),
#         'title': title.title(),
#         }
#     if tracks:
#         album_dict['tracks'] = tracks
#     return album_dict

# # Prepare the prompts.
# artist_name = "what is the artists' name?: "
# song_title = "what is the title of the song?: "
# track_no = "how many tracks are on the album?: "

# while True:
#     artist = input(artist_name)
#     if artist == 'quit':
#         break

# def greet_users(names):
#     for name in names:
#         message = f"Hello {name.title()}"
#         print(message)

# usernames = ['jack', 'sparrow', 'billal']

# greet_users(usernames)

# #start with some designs that need to be printed
# unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
# completed_models = []

# #simulate printing each design, until none are left
# #move each design to completed_models after printing

# while unprinted_designs:
#     current_design = unprinted_designs.pop()
#     print(f"Printing model: {current_design}")
#     completed_models.append(current_design)

# #display all completed models.
# print("\nThe following models have been printed:")
# for completed_model in completed_models:
#     print(completed_model)

#revising chapter 8: functions
# def greet_user():
#     print("welcome to the revision of chapter 8 :)")

# greet_user()

#passing information into a function:
# def greet_user(name):
#     print(f"{name}, welcome to the revision of chapter 8 :)")

# greet_user('suwayne')

#8-1 message: 
# def display_message():
#     print("im currently learning functions")

# display_message()

# def favorite_book(title, author):
#     print(f"one of my fav books is {title}, by {author}")

# favorite_book('the alchemist', 'paulo coelho')

# def describe_pet(name, breed ='gsd'):
#     print(f"my dogs name is {name}, and it's a {breed}")


# describe_pet('rocky', breed = 'rot')

"""
8-3. T-Shirt: Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt. 
The function should print a sentence summarizing the size of the shirt and the message printed on it.
Call the function once using positional arguments to make a shirt. Call the function a second time using keyword arguments.
"""
# def make_shirt(size, message_text):
#     print(f"this shirt is a size {size}.")
#     print(f"{message_text}")

# make_shirt(8, 'welcome to the new world order')

# def get_formattedname(first_name, last_name):
#     full_name = f"{first_name} {last_name}"
#     return full_name.title()

# player1 = get_formattedname('osasu', 'ogbebor')
# print(player1)

# def get_formattedname(first_name, middle_name, last_name=''): #optional parameters should come last
#     full_name = f"{first_name} {middle_name} {last_name}"
#     return full_name

# player1 = get_formattedname('osasu', 'ehi')
# print(player1)


# def build_person(first_name, last_name, age = None):
#     person = {'first': first_name, 'last': last_name}
#     if age:
#         person['age'] = age
#     return person

# player1 = build_person('osasu', 'ogbebor', 30)
# print(player1)

# def get_formatted_name(first_name, last_name):
#     """Return a full name, neatly formatted."""
#     full_name = f"{first_name} {last_name}"
#     return full_name.title()

# while True:
#     print("\nPlease tell me your name:")

#     f_name = input("First name: ")
#     if f_name == 'quit':
#         break
#     l_name = input("Last name: ")
#     if l_name == 'quit':
#         break

#     formatted_name = get_formatted_name(f_name, l_name)
#     print(f"\nHello, {formatted_name}!")

# #ex8_6
# def city_country(city, country):
#     location = f"I live in {city.title()}, and it is located in {country.upper()}."
#     return location

# place1 = city_country('lagos', 'nigeria')
# print(place1)

# #ex8_7

# def make_album(artist_name, album_title):
#     record = {
#         'artist': artist_name,
#         'album': album_title,
#     }
#     print(record) 

# album1 = make_album('michael jackon', 'bad')
# print(album1)

# #ex8_8
# def make_album(artist_name, album_title, song_no = None):
#     record = {
#         'artist': artist_name,
#         'album': album_title,
#     }
#     if song_no:
#         record['songs'] = song_no       #dictionary name[key] = value
#     return record

# print("Ps. answer the prompts")
# print("Enter 'quit' to cancel the program.")

# while True:
#     artist_name = input("\nEnter the artists name: ")
#     if artist_name == 'quit':
#         break

#     album_title = input("Enter the albums title: ")
#     if album_title == 'quit':
#         break

#     song_no = input("Enter the number of songs: ")
#     if song_no == 'quit':
#         break
    
#     result1 = make_album(artist_name, album_title, song_no)
#     print(result1)

#passing a list
# def greet_users(names):
#     for name in names:
#         print(f"Welcome to the party, {name.title()}")

# poll = ['david', 'vado', 'burna', 'killaman', 'brymo']
# greet_users(poll)


class Employee:
    def __init__(self, first, last, pay):                       #this is a class
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@ecompany.com'

    def fullname(self):                                         #this is a method
        return '{} {}'.format(self.first, self.last)



    
emp_1 = Employee('osasu', 'ogbebor', 500000)                    #this is an instance of a class
emp_2 = Employee('iyayi', 'ogbebor', 400000)


print(emp_2.fullname())