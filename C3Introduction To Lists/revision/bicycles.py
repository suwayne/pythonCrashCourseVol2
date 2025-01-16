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
# motorcycle = ['honda', 'ducati', 'suzuki']
# print(motorcycle)

# motorcycle[0] = 'tesla'

# print(motorcycle)

# motorcycle.append('yamaha')
# print(motorcycle)

# motorcycle = []

# motorcycle.append('honda')
# motorcycle.append('yamaha')
# motorcycle.append('ducatti')
# motorcycle.append('mercedez')


# print(motorcycle)


# motorcycle = ['honda', 'yamaha', 'suzuki']
# #adding items to any location in your list
# motorcycle.insert(1, 'ducati')
# print(motorcycle)

#removing items from the list

# motorcycle = ['honda', 'yamaha', 'suzuki']
# print(motorcycle)

# del motorcycle[0]
# print(motorcycle)

# pop a motocycle from a list of motorcycle

motorcycle = ['honda', 'yamaha', 'suzuki']
print(f"The motorcycle: {motorcycle}")

# popped_motorcycle = motorcycle.pop() #this shows you the pop method takes the last item from the list to work with
# print(f"The popped motocycles: {popped_motorcycle}")

# last_owned = popped_motorcycle
# print(last_owned)

# print(f"The last motorcycle I owned was a {last_owned} 2018 model.")

# first_owned = motorcycle.pop(0)
# print(first_owned)


#remove method
motorcycle.remove('yamaha')
print(f"Testing the remove method: {motorcycle}")

#alternatively
too_expensive = 'honda'
motorcycle.remove(too_expensive)
print(f"This selected {motorcycle} is expensive")




