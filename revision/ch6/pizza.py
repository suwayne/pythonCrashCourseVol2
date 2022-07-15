#store information about a pizza being stored. 

pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}

#summarize the order.
print(f"you have ordered a {pizza['crust']} crusted pizza."
    "with the following toppings:")

for topping in pizza['toppings']:
    print("\t" + topping.title())



