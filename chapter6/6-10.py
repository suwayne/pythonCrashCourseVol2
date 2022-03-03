favorite_numbers = {
    'iyayi': [9, 40, 20],
    'nayin': [6, 43, 20],
    'osasu': [45, 60, 10],
    'desola': [357, 4432, 20],
    'ehis': [923, 4045, 202],
}

for key, values in favorite_numbers.items():
    print(key)
    for value in values:
        print("\t" + str(value))
