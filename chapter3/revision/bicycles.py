bicycles = ['trek', 'cannondale', 'specialized']
#print(bicycles) here you printed all the items in the list
#print(bicycles[0]) here you printed the first item on the list

#using fstring and a method with the list.
#message = f"My first bicycle was a {bicycles[1].title()}." 

#print(message)


#ex1 Printing each of your friends names from the list
# names = ['Nayin', 'Dele', 'Ita', 'chidera']

# # print("Here's a list of your men dem.")
# # print(names[1])
# # bestman = f"My bestman for the day will definitely be {names[0]}, but sadly he won\'t make it due to family commitments."
# # likemind = f"One like minded individual I truely respect is {names[3]}, he\'s an absolute gentleman and a no bs individual."


# # print(bestman)
# # print(likemind)

# #ex2 
# greeting = f"Have a merry christmas and may your days be bright {names[3]}" 

# print(greeting)

#ex3
# transportType = ['motorcycle', 'car', 'truck', 'boat']
# message = f"I would love to own a {transportType[0]}"


# print("I would love to own a " + transportType[0])

#myExample

# first_name = "osasu"
# last_name = "ogbebor"

# full_name = f"{first_name} {last_name}"

# print(full_name)

#changing an item on the list
# motorcycles = ['honda', 'ducati', 'suzuki']
# print(motorcycles)

# motorcycles[0] = 'tesla'

# print(motorcycles)

# motorcycles.append('yamaha')
# print(motorcycles)

# motorcycles = []

# motorcycles.append('honda')
# motorcycles.append('yamaha')
# motorcycles.append('ducatti')
# motorcycles.append('mercedez')


# print(motorcycles)


# motorcycles = ['honda', 'yamaha', 'suzuki']
# #adding items to any location in your list
# motorcycles.insert(1, 'ducati')
# print(motorcycles)

#removing items from the list

# motorcycles = ['honda', 'yamaha', 'suzuki']
# print(motorcycles)

# del motorcycles[0]
# print(motorcycles)

# pop a motocycle from a list of motorcycles

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(popped_motorcycle)

last_owned = popped_motorcycle
print(last_owned)

