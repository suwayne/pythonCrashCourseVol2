"""
favorite places exercise
"""

favorite_places = {
    'iyayi': ['miami', 'tunisia', 'france'],
    'osasu': ['abu dhabi', 'seychelles','argentina'],
    'mosope': ['texas', 'massachusettes', 'morocco'],

}
print("Exercise 6_9.py: Favorite places:")
for name, places in favorite_places.items():
    print(f"{name} loves to visit the following places:")
    for place in places:
        print(f"- {place.title()}")



