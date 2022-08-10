"""
Write a function called city_country() that takes in the name of a city and its country. The function 
should return a string formatted like this: "Santiago, Chile
"""

# def country(city, country):
#     location = f"{city}, {country}"
#     return location.title()

# vacation = country('takamaka', 'seychelles')
# vacation1 = country('dubai', 'uae')
# vacation2 = country('nova scotia', 'canada')

# print(vacation)
# print(vacation1)
# print(vacation2)


def country(city, country):
    location = f"{city}, {country}"
    print(location.title())

vacation = country('takamaka', 'seychelles')
vacation1 = country('dubai', 'uae')
vacation2 = country('nova scotia', 'canada')
