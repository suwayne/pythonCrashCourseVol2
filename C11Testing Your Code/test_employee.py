import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):
    # test for the employee module
    def setUp(self):
        # make an employee to use in tests
        self.eric = Employee('eric', 'matthes', 65_000)

    def test_give_default_raise(self):
        # test that a default raise works correctly
        self.eric.give_raise()
        self.assertEqual(self.eric.annual_salary, 70000)

    def test_give_custom_raise(self):
        # test that a custom raise works correctly
        self.eric.give_raise(10000)
        self.assertEqual(self.eric.annual_salary, 75000)


if __name__ == '__main__':
    unittest.main()
