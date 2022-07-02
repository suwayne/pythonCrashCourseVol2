#using the name of the list 'requested toppings' in the if statement, will evaluate to true, if there's at least
# one item in the list.
# or if it's false it'll skip the rest of the code and print out the else statement. 

requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}")
    print("\nfinished making your pizza!")

else: 
    print("are you sure you want a plain pizza?")

