import math
import unittest

from operations import *


class TestBasicOperations(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(subtract(10, 4), 6)

    def test_multiply(self):
        self.assertEqual(multiply(6, 7), 42)

    def test_divide(self):
        self.assertEqual(divide(20, 5), 4)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide(10, 0)


class TestPowersAndRoots(unittest.TestCase):

    def test_square(self):
        self.assertEqual(square(5), 25)

    def test_cube(self):
        self.assertEqual(cube(3), 27)

    def test_root(self):
        self.assertEqual(root(81), 9)

    def test_negative_root(self):
        with self.assertRaises(ValueError):
            root(-1)

    def test_cube_root_positive(self):
        self.assertEqual(cube_root(27), 3)

    def test_cube_root_negative(self):
        self.assertEqual(cube_root(-8), -2)

    def test_power_integer_exponent(self):
        self.assertEqual(power(2, 5), 32)

    def test_power_fractional_exponent(self):
        self.assertAlmostEqual(power(9, 0.5), 3)

    def test_negative_base_integer_exponent(self):
        self.assertEqual(power(-2, 3), -8)

    def test_negative_base_fractional_exponent(self):
        with self.assertRaises(ValueError):
            power(-2, 0.5)

    def test_zero_negative_power(self):
        with self.assertRaises(ZeroDivisionError):
            power(0, -1)


class TestUtilityOperations(unittest.TestCase):

    def test_percentage(self):
        self.assertEqual(percentage(25, 100), 25)

    def test_percentage_zero_base(self):
        with self.assertRaises(ZeroDivisionError):
            percentage(5, 0)

    def test_absolute(self):
        self.assertEqual(absolute(-42), 42)

    def test_random_int(self):
        value = random_int_gen(1, 10)

        self.assertGreaterEqual(value, 1)
        self.assertLessEqual(value, 10)

    def test_random_int_invalid_range(self):
        with self.assertRaises(ValueError):
            random_int_gen(10, 1)


class TestTrigonometry(unittest.TestCase):

    def test_sin(self):
        self.assertAlmostEqual(sin_deg(30), 0.5)

    def test_sin_zero(self):
        self.assertEqual(sin_deg(180), 0.0)

    def test_cos(self):
        self.assertAlmostEqual(cos_deg(60), 0.5)

    def test_cos_special(self):
        self.assertEqual(cos_deg(180), -1.0)

    def test_tan(self):
        self.assertAlmostEqual(tan_deg(45), 1.0)

    def test_tan_undefined(self):
        with self.assertRaises(ValueError):
            tan_deg(90)

    def test_asin(self):
        self.assertEqual(asin_deg(1), 90)

    def test_acos(self):
        self.assertEqual(acos_deg(1), 0)

    def test_atan(self):
        self.assertAlmostEqual(atan_deg(1), 45)

    def test_asin_invalid(self):
        with self.assertRaises(ValueError):
            asin_deg(2)

    def test_acos_invalid(self):
        with self.assertRaises(ValueError):
            acos_deg(-2)


class TestLogarithms(unittest.TestCase):

    def test_logn(self):
        self.assertAlmostEqual(logn(math.e), 1)

    def test_log10(self):
        self.assertEqual(log10(1000), 3)

    def test_log2(self):
        self.assertEqual(log2(1024), 10)

    def test_log(self):
        self.assertEqual(log(8, 2), 3)

    def test_logn_invalid(self):
        with self.assertRaises(ValueError):
            logn(0)

    def test_log10_invalid(self):
        with self.assertRaises(ValueError):
            log10(-5)

    def test_log2_invalid(self):
        with self.assertRaises(ValueError):
            log2(0)

    def test_log_invalid_base_zero(self):
        with self.assertRaises(ValueError):
            log(10, 0)

    def test_log_invalid_base_one(self):
        with self.assertRaises(ValueError):
            log(10, 1)


if __name__ == "__main__":
    unittest.main()
