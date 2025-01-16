# sandwiches
def sandwiches(*toppings):
    """print the summary of the sandwich being prepped"""
    for topping in toppings:
        print(topping)


print("First order:")
sandwiches('beef', 'chicken', 'mayonnaise')

print("\nSecond order:")
sandwiches('tuna', 'jam', 'spring onions')
