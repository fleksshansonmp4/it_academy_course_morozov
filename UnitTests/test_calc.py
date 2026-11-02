import unittest
from calc import add, sub, mul, div, power

class TestCalc(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_add(self):
        result = 1 + 2
        self.assertEqual(add(1,2), result)

    def test_sub(self):
        result = 3 - 5
        self.assertEqual(sub(3, 5), result)

    def test_mul(self):
        result = 2 * 5
        self.assertEqual(mul(2, 5), result)

    def test_div(self):
        result = 6 / 2
        self.assertEqual(div(6, 2), result)

    def test_div_zero(self):
        self.assertRaises(ZeroDivisionError, div, 10, 0)

    def test_pow(self):
        self.assertEqual(power(5,2), 5 ** 2)


if __name__ == "__main__":
    unittest.main(verbosity=2)