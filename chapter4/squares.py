# print square of each integer from 1 to 20

squares = []
for value in range(1, 21):
    square = value ** 2
    squares.append(square)

print(squares)

# concise version
squares = []
for value in range(1, 21):
    squares.append(value**2)

print(squares)

# list comprehension

squares = [value**2 for value in range(1, 11)]
print(squares)
