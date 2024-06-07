import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):

    def setUp(self):
        self.employee = Employee('tom', 'ackerley', 35_000)

    def test_give_default_raise(self):
        """teste para mostrar que o valor padrão funciona"""
        self.employee.give_raise()
        self.assertEqual(self.employee.annual_salary, 40_000)

    def test_give_custom_raise(self):
        """teste para que um aumento personalizado funciona"""
        self.employee.give_raise(10_000)
        self.assertEqual(self.employee.annual_salary, 45_000)

if __name__ == '__main__':
    unittest.main()