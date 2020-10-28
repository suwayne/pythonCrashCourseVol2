import unittest
from city_functions import get_city_country


class CityCountryTest(unittest.TestCase):

    def test_city_country(self):
        formatted_output = get_city_country(
            'lagos', 'nigeria', population=3_0000)
        self.assertEquals(formatted_output,
                          'Lagos, Nigeria - Population 30000')


if __name__ == '__main__':
    unittest.main()
