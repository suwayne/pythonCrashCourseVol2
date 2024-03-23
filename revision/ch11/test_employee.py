import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):

    def setUp(self):
        first_name = 'John'
        last_name = 'Doe'
        self.salary = 50000
        self.employee = Employee(first_name, last_name, self.salary)

    def test_give_default_raise(self):
        self.employee.give_raise()
        self.assertEqual(self.employee.salary, self.salary + 5000)

    def test_give_custom_raise(self):
        custom_raise = 10000
        self.employee.give_raise(custom_raise)
        self.assertEqual(self.employee.salary, self.salary + custom_raise)

if __name__ == '__main__':
    unittest.main()
    