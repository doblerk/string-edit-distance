import unittest
from sed.string_edit_distance import StringEditDistance


class TestStringEditDistance(unittest.TestCase):
    
    def test_sed(self):
        string1 = 'ABABBB'
        string2 = 'BABAAA'

        n, m = len(string1), len(string2)

        sed = StringEditDistance(string1, string2)

        D = sed.init_cost_matrix()
        P = sed.init_pointer_matrix()

        sed.calc_sed(D, P)

        self.assertEqual(D[n, m], 6)

if __name__ == '__main__':
    unittest.main()