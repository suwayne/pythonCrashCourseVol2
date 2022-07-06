#print the square of numbers from 1 to 10

squares = []

for square in range(1, 11):
    value = (square ** 2) #single * operator would add two, double * operator would mutliply by 2
    squares.append(value)


print(squares)


squares = [value ** 2 for value in range(1, 11)]

print(squares)

