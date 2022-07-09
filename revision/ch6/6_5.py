
rivers = {
    'nile': 'egypt',
    'benue': 'nigeria',
    'manhattan': 'united states',
}

for river, country in sorted(rivers.items()):
    print(f"The {river.title()} runs through {country.title()}.")

print("---")

for river in rivers.keys():
    print(river.title())

print("---")

for country in rivers.values():
    print(country.title())






