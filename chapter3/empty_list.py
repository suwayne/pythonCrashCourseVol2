# append items to an empty list
motorcycles = []

motorcycles.append('suzuki')
motorcycles.append('honda')
motorcycles.append('mercedez')
motorcycles.append('scooter')

print(motorcycles)

# delete the last item on the list
del motorcycles[-1]
print(motorcycles)
# removing the last item from a list using pop() method
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

print(motorcycles)
# removing the first item from a list and storing the value in 'first_motocycle
first_motocycle = motorcycles.pop(0)

print(first_motocycle)
