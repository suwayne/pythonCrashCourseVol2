"""
favorite places exercise
"""

favorite_places = {
    'iyayi': ['miami', 'tunisia', 'france'],
    'osasu': ['abu dhabi', 'seychelles','argentina'],
    'mosope': ['texas', 'massachusettes', 'morocco'],

}
print("Exercise 6_9.py: Favorite places:")
for name, places in favorite_places.items():        #you decleared a key value pair for the dictionary here
    print(f"{name} loves to visit the following places:")       #printing the keys in the dictionary at this point
    for place in places:        #this line loops through every 'value' in the dictionary, list mode :)
        print(f"- {place.title()}")



