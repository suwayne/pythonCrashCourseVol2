#exercise 6_12, extensions:
cities = {
    'lagos':{
        'country': 'nigeria',
        'population': 350000000,
        'fact': 'the miami of africa',
        'race': 'african',
    },
    'dubai':{
        'country': 'uae',
        'population': 9000000,
        'fact': 'a giant human sized amusement park',
        'race': 'asian',
    },
    'paris':{
        'country': 'france',
        'population': 70000000,
        'fact': 'the great eiffel tower stands tall here',
        'race': 'european',
    },
}
"""
At this point, following the text, and exercises at the end of the chapter, i figured out how to loop through key/ value pairs
effectively. Gotta find more places to practice this :)
"""
for key, value in cities.items():
    print(f"A few fun facts about {key.title()}")
    for va, val in value.items():
        print(f"- {va.title()}: {val}")

