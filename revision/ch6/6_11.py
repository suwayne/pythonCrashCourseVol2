"Exercise 6_11: Cities"
cities = {
    'lagos':{
        'country': 'nigeria',
        'population': 350000000,
        'fact': 'the miami of africa',
    },
    'dubai':{
        'country': 'uae',
        'population': 9000000,
        'fact': 'a giant human sized amusement park',
    },
    'paris':{
        'country': 'france',
        'population': 70000000,
        'fact': 'the great eiffel tower stands tall here',
    },
}
"""
At this point, following the text, and exercises at the end of the chapter, i figured out how to loop through key/ value pairs
effectively. Gotta find more places to practice this :)
"""
for key, value in cities.items():
    print(key)
    for val in value:
        print(f"- {val}")




