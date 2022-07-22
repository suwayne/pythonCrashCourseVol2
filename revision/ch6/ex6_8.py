
pets = []

pet1 = {
    'breed': 'gsd',
    'owners name': 'osasu ogbebor',
    'weight': 45,
}

pet2 = {
    'breed': 'poodle',
    'owners name': 'iyayi vivian',
    'weight': 87,
}

pet3 = {
    'breed': 'dalmatian',
    'owners name': 'jude okosun',
    'weight': 42
}

pets.append(pet1)
pets.append(pet2)
pets.append(pet3)

#taking a look at all the pets added to the list.
print(pets)

for pet in pets: 
    details = f"this {pet['breed']} weights {pet['weight']}, and is owned by {pet['owners name']}."
    print(details)

