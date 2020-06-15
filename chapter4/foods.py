my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

print("my favorite foods are:")
print(my_foods)

print("\nMy friends favorite foods are:")
print(friend_foods)

my_foods.append('canoli')
friend_foods.append('ice cream')

print("My friends foods are:")
print(friend_foods)
print("My foods are:")
print(my_foods)

print("\nthe first three items on my friends food list are:")
# print(friend_foods[0:])
for food in my_foods[0:3]:
    print(food)

# print("the last two items on my food list are:")
# print(my_foods[-2:])
