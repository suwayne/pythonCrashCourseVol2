# #python>introduction>loops
# def loop(n=30):
#     # n = int(input('enter a number: '))      
#     for i in range(1, n+1):
#         print(i, end = ',')

# # loop(4)
# loop()

def squares():
    squares = [value ** 2 for value in range(1, 21)]
    return squares

print(squares())
