# favorite places

favorite_places = {
    'osasu': ['dubai', 'canada', 'new zealand'],
    'desola': ['china', 'germany', 'spain'],
    'iyayi': ['mauritius', 'singapore', 'london'],
}

for name, places in favorite_places.items():
    print("name: " + name.title())
    for place in places:
        print("\t" + place)
