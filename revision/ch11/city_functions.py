"""
City, Country: Write a function that accepts two parameters: a city name and a country name. The 
function should return a single string of the form City, Country, such as Santiago, Chile. Store 
the function in a module called city_functions.py.
"""
def cityCountry(city, country):
    full_title = f"{city} {country}"
    return full_title.title()

