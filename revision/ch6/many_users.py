users = {   #this is the dictionary housing two nested keys.
    'aeinstein': {              #this is key 1.
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
        },

    'mcurie': {                 #this is key 2.
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
        },
}

for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']

    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")
