import unittest
from city_functions import city_country

class CitiesTestCase(unittest.TestCase):

    def test_city_country(self):
        formatted = city_country('porto', 'portugal')
        self.assertEqual(formatted, 'Porto, Portugal')

    def test_city_country_population(self):
        # incluindo o argumento opcional 'population'
        formatted = city_country('porto', 'portugal', 100_000)
        self.assertEqual(formatted, 'Porto, Portugal - population 100000')

if __name__ == '__main__':
    unittest.main()