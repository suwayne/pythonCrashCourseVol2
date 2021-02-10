from die import Die

#create D6
die = Die()

#make some rolls and store the result in a list
results = []
for rull_num in range(100):
    result = die.roll()
    results.append(result)

print(results)

