pizzas = ['magarita', 'suya', 'beef']
for pizza in pizzas:
    print("I like " + pizza.title() + " pizza.")

print("I enjoy eating pizza because it is tasty, and i enjoy flavours like " +
      pizzas[0].title() + ", " + pizzas[1].title() + " and " + pizzas[2].title() + "\n")

friend_pizzas = pizzas[:]

pizzas.append('plantain suya')
friend_pizzas.append('nakamura')

print("my favourite pizzas are;")
for pizza in pizzas:
    print(pizza.upper())

print("\nmy friends favourite pizzas are;")
for chow in friend_pizzas:
    print(chow.upper())
