import unittest
from city_functions import city_country

class CitiesTestCase(unittest.TestCase):

    def test_city_country(self):
        formatted = city_country('porto', 'portugal')
        self.assertEqual(formatted, 'Porto, Portugal')

if __name__ == '__main__':
    unittest.main()