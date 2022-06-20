reptiles = ['snake', 'crocodile', 'lizard','wall gecko']

# print("here is a list of reptiles i have found in my locality:")
# for reptile in reptiles:
#     print(reptile)

# for reptile in reptiles:
#     print(f"a {reptile} will make a great pet.")

# print("All listed animals above are reptiles.")

print(f"the first 3 items in the list are: {reptiles[0:3]}")
print(f"two items from the middle of the list are {reptiles[1:3]}")
print(f"the last item in the list is {reptiles[3:]}")


"""
4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1 (page 56). 
Make a copy of the list of pizzas, and call it friend_pizzas. Then, do the following:
"""

pizzas = ['beef bbq', 'magarita', 'pepperoni']
pizzas.append('dodo pizza')

friendPizzas = pizzas[:]
friendPizzas.append('hawaian')

print("my favorite pizzas are:")
for pizza in pizzas:
    print(pizza)

print("\nmy friends favorite pizzas are:")
for friend in friendPizzas:
    print(friend) #printing the list with a for loop.


print("\nmy friends favorite pizzas are:")
print(friendPizzas) #printing the list as it is to save space.









