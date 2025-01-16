# rental car
# car = input("what kind of rental car would you like? ")
# print(" >let me see if i can find you a " + car + ".")

# restaurant seating
# dgroup = input("how many people are in your dinner group? ")
# dgroup = int(dgroup)

# if dgroup > 8:
#     print("you'll have to wait for a table.")
# else:
#     print("your table is ready.")

# multiples of 10
# number = input("enter a random number: ")
# number = int(number)

# if number % 10 == 0:
#     print("this number is a multiple of 10.")
# else:
#     print("this number isn't a multiple of 10.")

# current_number = 1
# while current_number <= 5:
#     print(current_number)
#     current_number += 1

# parrot.py

# prompt = "\nTell me something, and I will repeat it back to you."
# prompt += "\nEnter 'quit' to end the program: "

# message = ""
# while message != 'quit':
#     message = input(prompt)

#     if message != 'quit':
#         print(message)


# parrot.py using flags

# prompt = "\n Tell me something and I will repeat it back to you."
# prompt += "\nEnter quit to end the program."

# active = True
# while active:
#     message = input(prompt)

#     if message == 'quit':
#         active = False
#     else:
#         print(prompt)

# using break to exit a loop

# prompt = "enter the name of a city."
# prompt += "enter quit to exit."

# while True:
#     city = input(prompt)

#     if city == 'quit':
#         break
#     else:
#         print("id love to go to " + city.title() + ".")

# current_number = 0
# while current_number < 10:
#     current_number += 1
#     if current_number % 2 == 0:
#         continue
#     print(current_number)

# 7-4 pizza toppings
# prompt = "\nenter a pizza topping."
# prompt += "\nenter quit to exit:"

# message = ""
# while message != 'quit':
#     message = input(prompt)
#     if message != 'quit':
#         print("I will add " + message + " topping to your pizza.")

# 7-4 version 2
# prompt = "Enter pizza topping and i'll repeat it to you"
# prompt += "Enter quit to end the program: "

# message = ""
# while message != 'quit':
#     message = input(prompt)

#     if message != 'quit':
#         print(message)

# 7-4 version 3
# prompt = "\nEnter pizza topping and i'll repeat it to you"
# prompt += "\nEnter quit to end the program: "

# active = True
# while active:
#     message = input(prompt)
#     if message == 'quit':
#         break
#         # active = False
#     else:
#         print(message)

# 7-6 The Infinity loop
# x = 1
# while x < 6:
#     print(x)


# 7-5 line to accept users age
# age = int(input("what is your age: "))
# if age <= 3:
#     print("the movie ticket is free.")
# elif age >= 3 and age <= 12:
#     print("the movie ticket is $10.")
# elif age > 12:
#     print("the movie ticket is $15.")

# 7-6 three exits

# # 7-7 loop that never ends
# number = 1
# while number < 5:
#     print(number)

# deli
# sandwich_orders = ['peanut butter', 'peanut butter and jelly',
#                    'mayonnaise', 'chicken mayonnaise', 'beef']
# finished_sandwiches = []

# for sandwich in sandwich_orders:
#     print(sandwich)

# #the enumerate function
# fruit = ['banana', 'apple', 'pear', 'peach']
# for i, item in enumerate(fruit, 1):
#     print(i, '. ' + item, sep='', end='\n')

prompt = "how old are you?"
prompt += "\nenter quit when you are finished: "

while True:
    age = input(prompt)
    if age == 'quit':
        break

    age = int(age)
    if age < 3:
        print("you get in free")
    elif age < 13:
        print("your ticket is $10")
    else:
        print("your ticket is $15")
