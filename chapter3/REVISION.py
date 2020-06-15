# completed revision
"""
laptops = ['macbook', 'toshiba', 'dell', 'ibm', 'lenovo']
print(laptops)
print(laptops[0].title())
print(laptops[4].upper())
print(laptops[-1])
message = "My first laptop was a " + laptops[2].title() + "."
print(message)

laptops.append('acer')
print(laptops)

laptops.append('chromebook')
# adding items to a list using the .extend() method
new_laptops = ['samsung', 'linux', 'alienware']
laptops.extend(new_laptops)
print(laptops)

# inserting items to a position on a list
laptops.insert(0, 'jedibook')
print(laptops)

# deleting an item from a list
del laptops[-1]
print(laptops)

popped_laptops = laptops.pop()
print(laptops)
print(popped_laptops)

print("the last owned laptop i had was a " + popped_laptops.title() + ".")

# removing itmes from a specific position
first_owned = laptops.pop(0)
print("the first laptop i owned was a " + first_owned + ".")
print(laptops)

# remove items from a list using its value or name
laptops.pop()
print(laptops)

last_owned = laptops.pop()
print(laptops)
print("My last laptop was a " + last_owned + ".")

first_owned = laptops.pop(-1)
print(first_owned)

print(laptops)

laptops.remove('toshiba')
print(laptops)
# post chapter 3 exercise
guest_list = ['michael jackson', 'dad', 'bob marley', 'fela kuti']
michael = guest_list[0]
pops = guest_list[1]
reggae = guest_list[2]

print("Hello " + michael + " please come around for dinner")
print("Hello " + pops + " please come around for dinner")
print("Hello " + reggae + " please come around for dinner")

absent = guest_list.pop()
print(guest_list)

print("\nWe are sorry to announce that " + absent +
      " will not be making it to the event" + ".")

new_guest = guest_list.append('lagbaja')

print(guest_list)
print("\nWe will be inviting " + str(len(guest_list)) + " people to the party.")

print("\nThe new guest will be " + guest_list[-1] + ".")

print("\nHello " + michael + " please come around for dinner")
print("Hello " + pops + " please come around for dinner")
print("Hello " + guest_list[-1] + " please come around for dinner")

print("\nHello everyone, we found a bigger dinner table ")
guest_list.insert(0, 'vader')
print(guest_list)

guest_list.insert(3, 'bruce lee')
guest_list.append('kevin spacey')

print(guest_list)

print("\nHello " + michael + " please come around for dinner")
print("Hello " + pops + " please come around for dinner")
print("Hello " + guest_list[-1] + " please come around for dinner")

print(guest_list)

print("\n Hello everyone, only 2 people will be invited")
guest_list.pop()
print(guest_list)
guest_list.pop()
guest_list.pop()
guest_list.pop()
guest_list.pop()

print(guest_list)

print("\nYou are invited to atted Mr. " + guest_list[0].title())
print("You are invited to atted Mr. " + guest_list[1].upper())

del guest_list[0]
print(guest_list)

del guest_list[0]
print(guest_list)

# sorting

cars = ['honda', 'toyota', 'mercedez', 'acura']
cars.sort()
print(cars)

cars.sort(reverse=True)
print(cars)

# using the sorted function

cars = ['honda', 'toyota', 'mercedez', 'acura']
print("\nHere is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the original list again:")
print(cars)

# revers chronological order
print(cars)

cars.sort()
print(cars)

cars.sort(reverse=True)
print(cars)

print(len(cars))
# seeing the world exercise

destinations = ['Kenya', 'Cape verde', 'Canada', 'France', 'Gernamy']
print(destinations)
print(sorted(destinations, reverse=True))

print(destinations)
destinations.reverse()
print(destinations)
destinations.reverse()
print(destinations)
destinations.sort()
print(destinations)
destinations.sort(reverse=True)
print(destinations)
"""
