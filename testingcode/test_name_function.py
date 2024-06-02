import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """teste para a função 'name_function'"""
    def test_first_last_name(self):
        full_name = get_formatted_name('margot', 'robbie')
        self.assertEqual(full_name, 'Margot Robbie')
    
    def test_first_last_middle_name(self):
        full_name = get_formatted_name('anya', 'joy', 'taylor')
        self.assertEqual(full_name, 'Anya Taylor Joy')

if __name__ == '__main__':
    unittest.main()