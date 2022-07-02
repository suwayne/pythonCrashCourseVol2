from urllib import request


requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding{requested_topping}")
    print("\nfinished making your pizza!")

else: 
    print("are you sure you want a plain pizza?")

