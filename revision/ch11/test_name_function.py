import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):

    def test_first_last_name(self):
        formatted_name = get_formatted_name('james', 'blunt')
        self.assertEqual(formatted_name, 'James Blunt')

    def test_first_last_middle_name(self):
        formatted_name = get_formatted_name('james', 'igwe', 'blunt')
        self.assertEqual(formatted_name, 'James Blunt Igwe')

if __name__ == '__main__':
    unittest.main()

