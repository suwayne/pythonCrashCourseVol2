# store information about pizza being ordered.

pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}

# summarize your order

print("you ordered a " + pizza['crust'] +
      "-crust pizza" + " with the following toppings:")

for topping in pizza['toppings']:
    print("\t" + topping)
