# #fizzbuzz challenge.

# for number in range(1, 101):
#     if number % 3 == 0 and number % 5 == 0:
#         print(f"{number} is a multiple of 3 and 5")
#     elif number % 5 == 0:
#         print(f"{number} is a multiple of 5")
#     elif number % 3 == 0:
#         print(f"{number} is a multiple of 3")

#     else:
#         print(number)
  

# length = input("input length: ")
# width = input("input width: ")

# area = int(length) * int(width)

# # print(f"the area is: {area}")
# print("the area is: " + str(area))


# length = int(input("input length: "))
# width = int(input("input width: "))

# area = length * width

# print(f"the area is: {area}")

# number = 2

# print(number + 1)

# alien_0 = {'color': 'green', 'speed': 'slow'}

# print(alien_0['points'])

alien_0 = {'color': 'green', 'speed': 'slow'}

point_value = alien_0.get('points', 'no point value assigned.') #this is what you do to return a message if the key you've requested
                                                                #does not exist.
print(point_value)

