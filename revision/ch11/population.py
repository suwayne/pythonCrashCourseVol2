"""
Modify your function so it requires a third parameter, population. It should now return 
a single string of the form City, Country population xxx, such as Santiago, Chile population 5000000. 
Run test _cities.py again. Make sure test_city_country() fails this time.
Modify the function so the population parameter is optional. Run test _cities.py again, 
and make sure test_city_country() passes again.
Write a second test called test_city_country_population() that veri- fies you can call 
your function with the values 'santiago', 'chile', and 'population=5000000'. Run test_cities.py again, 
and make sure this new test passes.
"""

def cityCountryPopulation(city, country, population=''):
    full_title = f"{city} {country} population: {population}"
    return full_title.title()

osasu = cityCountryPopulation('lagos', 'nigeria', 54000)
print(osasu)
