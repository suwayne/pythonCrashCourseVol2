users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}

for key, value in users.items():
    print(key + ":")
    full_name = value['first'] + " " + value['last']
    location = value['location']
    print("\t" + full_name)
    print("\t" + location)
