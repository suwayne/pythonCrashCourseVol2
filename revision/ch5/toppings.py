requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

# if 'mushrooms' in requested_toppings: 
#     print("Adding mushrooms.")
# if 'pepperoni' in requested_toppings: 
#     print("Adding pepperoni.")
# if 'extra cheese' in requested_toppings: 
#     print("Adding extra cheese.")
                 
                 
#making the code more efficient. 
# for requested_topping in requested_toppings:
#     print(f"Adding {requested_topping}.")

# print("\nfinished making your pizza!")


#what if pizzeria runs out of green peppers?

for requested_topping in requested_toppings:
    if requested_toppings == "green peppers":
        print("sorry, we are out of peppers right now.")
    else:
        print(f"adding {requested_topping}.")


print("\nfinished making your pizza!")








