"""
Write a function called describe_city() that accepts the name of a city and its country. The function should print a simple 
sentence, such as Reykjavik is in Iceland. Give the parameter for the country a default value. Call your function for three 
different cities, at least one of which is not in the default country.
"""

def describe_city(city_name, country):
    """prints simple sentence about countries and their cities."""
    print(f"\nThe city of {city_name} is in {country}.")

describe_city('Lagos', 'Nigeria')


