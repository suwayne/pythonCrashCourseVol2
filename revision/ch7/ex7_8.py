#exercise 7_8: Deli
"""
Make a list called sandwich_orders and fill it with the names of 
various sandwiches. Then make an empty list called finished_sandwiches.
Loop through the list of sandwich orders and print a message for each 
order, such as I made your tuna sandwich. As each sandwich is made, move 
it to the list of finished sandwiches. After all the sandwiches have 
been made, print a message listing each sandwich that was made.
"""
sandwich_orders = ['chicken sandwich', 'tuna sandwich', 'turkey sandwich', 'beef sandwich']
finished_sandwiches = []

for sandwich in sandwich_orders:
    print(f"I made your {sandwich} order.")

while sandwich_orders:
    made_sandwich = sandwich_orders.pop()
    finished_sandwiches.append(made_sandwich)

print("\n#Here's a list of finished sandwich orders:")
for finished in finished_sandwiches:
    print(finished.title())

