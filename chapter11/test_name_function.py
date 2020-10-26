import unittest
from name_function import get_formatted_name


class NamesTestCase(unittest.TestCase):
    # Tests for 'name_function.py
    def test_first_last_name(self):
        # do names like Janis Joplin work?
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_first_last_middle_middle(self):
        # check if names like 'wolfgang amadeus zeus works'
        formatted_name = get_formatted_name('wolfgang', 'zeus', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Zeus')


if __name__ == '__main__':
    unittest.main()
