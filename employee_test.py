import unittest
from employee_class import Employee


class EmployeeTest(unittest.TestCase):
    def setUp(self):
        self.petter = Employee('petter', 'eriksson', 500000)
        self.borje = Employee('börje', 'kurtsson', 15000)

    def test_give_default_raise(self):
        self.petter.give_raise()
        self.assertEqual(self.petter.salary, 505000)

    def test_give_custom_raise(self):
        self.borje.give_raise(500)
        self.assertEqual(self.borje.salary, 15500)


if __name__ == '__main__':
    unittest.main()
