cubes = [x ** 3 for x in range(1, 11)]
print(cubes)

# method 2
cubes = []
for x in range(1, 11):
    cube = x ** 3
    cubes.append(cube)

print(cubes)
