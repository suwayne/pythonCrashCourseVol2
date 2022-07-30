"""
Using the list sandwich_orders from Exercise 7-8, make sure the sandwich 'pastrami' appears in the list at least three times. Add code near the 
beginning of your program to print a message saying the deli has run out of pastrami, and then use a while loop to remove all occurrences of 
'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up in finished_sandwiches.
"""

sandwich_orders = ['pastrimi','chicken sandwich', 'pastrimi', 'tuna sandwich', 'turkey sandwich', 'pastrimi', 'beef sandwich']
finished_sandwiches = []

print("The deli has run put of pastrimi.")

while 'pastrimi' in sandwich_orders:
    sandwich_orders.remove('pastrimi')

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    finished_sandwiches.append(current_sandwich)

print("Here are the available sandwiches below: ")
for finished in finished_sandwiches:
    print(finished)



