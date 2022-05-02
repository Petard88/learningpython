import unittest
from city_functions import shitty_country

class shittytest(unittest.TestCase):
    def test_city_country(self):
        formatted_city_country = shitty_country('Örebro', 'Sverige')
        self.assertEqual(formatted_city_country, 'Örebro, Sverige.')

if __name__ == '__main__':
    unittest.main()