"""
Write a function that accepts a list of items a person wants on a sandwich. The function should have one parameter 
that collects as many items as the function call provides, and it should print a summary of the sand- wich thats 
being ordered. Call the function three times, using a different num- ber of arguments each time.
"""

def sandwich(*toppings):
    print("Here's a list of toppings on the sandwich:")
    for topping in toppings:
        print(f"  {topping}")

sandwich('chicken', 'beef', 'turkey', 'mayonnaise', 'samosa')

