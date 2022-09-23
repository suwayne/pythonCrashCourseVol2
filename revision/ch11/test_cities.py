"""
Create a file called test_cities.py that tests the function you just wrote (remember that you need 
to import unittest and the function you want to test). Write a method called test_city_country() to 
verify that calling your function with values such as 'santiago' and 'chile' results in the correct 
string. Run test_cities.py, and make sure test_city_country() passes.
"""
import unittest
from city_functions import cityCountry
from population import cityCountryPopulation

class NamesTestCase(unittest.TestCase):

    def test_city_country(self):
        formatted_name = cityCountry('santiago', 'chile')
        self.assertEqual(formatted_name, 'Santiago Chile')

    def test_city_country_population(self):
        formatted_name = cityCountryPopulation('santiago', 'chile', 30000)
        #what comes after formatted_name should be just like in the program you wrote :)
        self.assertEqual(formatted_name, 'Santiago Chile Population: 30000')


if __name__ == '__main__':
    unittest.main()
