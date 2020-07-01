def make_pizza(size, *toppings):
    print(f"making a {size} inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")
