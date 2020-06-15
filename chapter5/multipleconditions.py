# test equality and inequlity of strings
plane = 'boeing'
car = 'bmw'

if len(plane) == len(car):
    print("same number of alphabets")
else:
    print("not the same number of alphabets")

# test using Lower() function in command prompt
# if an item is in a list

cars = ['toyota', 'honda', 'tesla', 'peugeot']
car = 'mercedez'

if car not in cars:
    print("we don't sell that brand here")
else:
    print("come and spend all of your money")


# item not in a list

ec = 'tesla'
if ec in cars:
    print("the almighty " + ec + "." + " the future is here, buy a piece of it.")
else:
    print("we will keep on waiting")

# simple if statements

age = 19
if age >= 18:
    print("\nyou are old enough to vote")
    print("have you registered?")

# if-else statements

age = 17
if age >= 18:
    print("\nYou are old enough to vote!")
    print("have you registered?")

else:

    print("\nSorry, you are too young to vote.")
    print("please register to vote as soon as you turn 1*")

# if-elif-else chain statements
requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
    print("\nAdding mushrooms")
if 'peperoin' in requested_toppings:
    print("Adding peperoni")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese")
print("\nFinished making your pizza!")
