import unittest

# Чтобы фукнци is_even работала, необходимо было скорректировать условие проверки.

def is_even(number):
    ''' Returns True if **number** is even or False if it is odd. '''
    return number % 2 == 0


class TestFactorize(unittest.TestCase):

    def test_wrong_types_raise_exception(self):
        self.assertRaises(TypeError, is_even, 'string')

    def test_float(self):
        test_case = [-1.5, 2.5, 5.4, -2.4]
        for x in test_case:
            with self.subTest(x=x):
                self.assertFalse(is_even(x))

    def test_even_positive(self):
        test_case = [2, 4, 6, 8, 10, 100, 150]
        for x in test_case:
            with self.subTest(x=x):
                self.assertTrue(is_even(x))

    def test_even_negative(self):
        test_case = [-2, -14, -30, -22, -6]
        for x in test_case:
            with self.subTest(x=x):
                self.assertTrue(is_even(x))

    def test_odd_positive(self):
        test_case = [5, 11, 43, 897, 57, 667, 459]
        for x in test_case:
            with self.subTest(x=x):
                self.assertFalse(is_even(x))

    def test_odd_negative(self):
        test_case = [-1, -15, -47, -69, -7]
        for x in test_case:
            with self.subTest(x=x):
                self.assertFalse(is_even(x))

if __name__ == "__main__":
    unittest.main()