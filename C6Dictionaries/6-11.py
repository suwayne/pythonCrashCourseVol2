cities = {
    'dubai': {
        'country': 'uae',
        'population': 10000,
        'fact': 'plenty money',
    },
    'lagos': {
        'country': 'nigeria',
        'population': 4000,
        'fact': 'fun place',
    },
    'venice': {
        'country': 'italy',
        'population': 3000,
        'fact': 'historic town',
    },
}

for city, facts in cities.items():
    print(city.title())
    country = facts['country']
    population = facts['population']
    fact = facts['fact']
    print("\tCountry: " + country.title())
    print("\tPopulation: " + str(population))
    print("\tfact: " + fact.title())
