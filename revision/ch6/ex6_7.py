persons = []

iyayi_vivian = {
    'first name': 'iyayi',
    'last name': 'ogbebor',
    'city': 'waltham',
}

osasu_ogb = {
    'first name': 'osasu',
    'last name': 'ogbebor',
    'city': 'lagos',
}

seyi_nayin = {
    'first name': 'mosope',
    'last name': 'nayin',
    'city': 'texas',
}

persons.append(iyayi_vivian)
persons.append(osasu_ogb)
persons.append(seyi_nayin)

for person in persons:
    name = f"{person['first name'].title()} {person['last name'].title()}" 
    city = f"{person['city']}"

    print(f"welcome {name}, all the way from {city.title()}.")






