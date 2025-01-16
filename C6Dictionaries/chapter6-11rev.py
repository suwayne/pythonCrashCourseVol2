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

for key, value in cities.items():
    print(key.title())
    for value in value.items():
        print("\t" + str(value))
