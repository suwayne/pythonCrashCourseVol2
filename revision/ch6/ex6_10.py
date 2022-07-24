#favorite numbers:
favorite_numbers = {
    'osasu': [9, 43, 20, 12],
    'elijah': [12, 42, 11, 42],
    'joshua': [4, 9, 35, 84],
    'esosa': [9, 23, 95, 32],
}

#print each persons name and number.
# for number in favorite_numbers:
#     print(number, '>', favorite_numbers[number])

for key, value in favorite_numbers.items():
    print(f"{key.title()}'s favorite numbers:")
    for val in value:
        print(f"- {val}")

