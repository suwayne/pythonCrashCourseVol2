my_foods = ['pizza', 'falafel', 'carrot cake']
friendFoods = my_foods[:] #here's how you copy a whole list using empty first and second index.

print("my favorite foods are:")
print(friendFoods)



my_foods = friendFoods[:]
my_foods.append('canoli')
friendFoods.append('ice cream')

print(my_foods)
