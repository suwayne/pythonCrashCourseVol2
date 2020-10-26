import unittest
from city_functions import get_city_country


class CityCountryTest(unittest.TestCase):

    def test_city_country(self):
        formatted_output = get_city_country('santiago', 'chile')
        self.assertEquals(formatted_output, 'Santiago Chile')
