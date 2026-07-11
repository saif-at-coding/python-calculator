import math
import unittest
from operations import (
    add,
    subtract,
    multiply,
    divide,
    square,
    cube,
    root,
    cube_root,
    power,
    percentage,
    absolute,
    random_int_gen,
    sin_deg,
    cos_deg,
    tan_deg,
    asin_deg,
    acos_deg,
    atan_deg,
    logn,
    log10,
    log2,
    log,
)


class TestCalculatorOperations(unittest.TestCase):

    # ---------- Basic Arithmetic ----------

    def test_add(self):
        self.assertEqual(add(2.0, 3.0), 5.0)
        self.assertEqual(add(-2.0, 3.0), 1.0)
        self.assertEqual(add(0.0, 0.0), 0.0)

    def test_subtract(self):
        self.assertEqual(subtract(10.0, 5.0), 5.0)
        self.assertEqual(subtract(5.0, 10.0), -5.0)

    def test_multiply(self):
        self.assertEqual(multiply(4.0, 5.0), 20.0)
        self.assertEqual(multiply(-2.0, 3.0), -6.0)
        self.assertEqual(multiply(0.0, 100.0), 0.0)

    def test_divide(self):
        self.assertEqual(divide(10.0, 2.0), 5.0)
        self.assertEqual(divide(5.0, 2.0), 2.5)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide(10.0, 0.0)

    # ---------- Powers ----------

    def test_square(self):
        self.assertEqual(square(5.0), 25.0)
        self.assertEqual(square(-5.0), 25.0)
        self.assertEqual(square(0.0), 0.0)

    def test_cube(self):
        self.assertEqual(cube(3.0), 27.0)
        self.assertEqual(cube(-3.0), -27.0)
        self.assertEqual(cube(0.0), 0.0)

    def test_power(self):
        self.assertEqual(power(2.0, 10.0), 1024.0)
        self.assertEqual(power(2.0, -3.0), 0.125)
        self.assertEqual(power(5.0, 0.0), 1.0)

    def test_power_zero_negative(self):
        with self.assertRaises(ZeroDivisionError):
            power(0.0, -2.0)

    def test_power_negative_fraction(self):
        with self.assertRaises(ValueError):
            power(-2.0, 0.5)

    # ---------- Roots ----------

    def test_square_root(self):
        self.assertEqual(root(25.0), 5.0)
        self.assertEqual(root(0.0), 0.0)

    def test_square_root_negative(self):
        with self.assertRaises(ValueError):
            root(-25.0)

    def test_cube_root(self):
        self.assertAlmostEqual(cube_root(27.0), 3.0)
        self.assertAlmostEqual(cube_root(-8.0), -2.0)
        self.assertAlmostEqual(cube_root(125.0), 5.0)
        self.assertAlmostEqual(cube_root(0.0), 0.0)

    # ---------- Percentage ----------

    def test_percentage(self):
        self.assertEqual(percentage(50.0, 200.0), 25.0)
        self.assertEqual(percentage(0.0, 100.0), 0.0)
        self.assertEqual(percentage(25.0, 50.0), 50.0)

    def test_percentage_zero_base(self):
        with self.assertRaises(ZeroDivisionError):
            percentage(50.0, 0.0)

    # ---------- Absolute ----------

    def test_absolute(self):
        self.assertEqual(absolute(-10.0), 10.0)
        self.assertEqual(absolute(10.0), 10.0)
        self.assertEqual(absolute(0.0), 0.0)

    # ---------- Random Integer Generator ----------

    def test_random_int(self):
        for _ in range(100):
            value = random_int_gen(1, 10)
            self.assertIsInstance(value, int)
            self.assertGreaterEqual(value, 1)
            self.assertLessEqual(value, 10)

    def test_random_invalid_range(self):
        with self.assertRaises(ValueError):
            random_int_gen(10, 1)

    # ------------- Trigonometry Functions ------------

    def test_sin(self):
        self.assertAlmostEqual(sin_deg(0), 0.0)
        self.assertAlmostEqual(sin_deg(30), 0.5)
        self.assertAlmostEqual(sin_deg(45), math.sqrt(2) / 2)
        self.assertAlmostEqual(sin_deg(60), math.sqrt(3) / 2)
        self.assertAlmostEqual(sin_deg(90), 1.0)
        self.assertAlmostEqual(sin_deg(180), 0.0)
        self.assertAlmostEqual(sin_deg(270), -1.0)
        self.assertAlmostEqual(sin_deg(360), 0.0)

    def test_cos(self):
        self.assertAlmostEqual(cos_deg(0), 1.0)
        self.assertAlmostEqual(cos_deg(30), math.sqrt(3) / 2)
        self.assertAlmostEqual(cos_deg(45), math.sqrt(2) / 2)
        self.assertAlmostEqual(cos_deg(60), 0.5)
        self.assertAlmostEqual(cos_deg(90), 0.0)
        self.assertAlmostEqual(cos_deg(180), -1.0)
        self.assertAlmostEqual(cos_deg(270), 0.0)
        self.assertAlmostEqual(cos_deg(360), 1.0)

    def test_tan(self):
        self.assertAlmostEqual(tan_deg(0), 0.0)
        self.assertAlmostEqual(tan_deg(30), 1 / math.sqrt(3))
        self.assertAlmostEqual(tan_deg(45), 1.0)
        self.assertAlmostEqual(tan_deg(60), math.sqrt(3))
        self.assertAlmostEqual(tan_deg(135), -1.0)
        self.assertAlmostEqual(tan_deg(180), 0.0)

    def test_tan_undefined(self):
        for angle in (90, 270, -90, 450):
            with self.assertRaises(ValueError):
                tan_deg(angle)

    def test_asin(self):
        self.assertAlmostEqual(asin_deg(-1), -90.0)
        self.assertAlmostEqual(asin_deg(-0.5), -30.0)
        self.assertAlmostEqual(asin_deg(0), 0.0)
        self.assertAlmostEqual(asin_deg(0.5), 30.0)
        self.assertAlmostEqual(asin_deg(1), 90.0)

    def test_acos(self):
        self.assertAlmostEqual(acos_deg(-1), 180.0)
        self.assertAlmostEqual(acos_deg(-0.5), 120.0)
        self.assertAlmostEqual(acos_deg(0), 90.0)
        self.assertAlmostEqual(acos_deg(0.5), 60.0)
        self.assertAlmostEqual(acos_deg(1), 0.0)

    def test_atan(self):
        self.assertAlmostEqual(atan_deg(-math.sqrt(3)), -60.0)
        self.assertAlmostEqual(atan_deg(-1), -45.0)
        self.assertAlmostEqual(atan_deg(0), 0.0)
        self.assertAlmostEqual(atan_deg(1), 45.0)
        self.assertAlmostEqual(atan_deg(math.sqrt(3)), 60.0)

    def test_asin_invalid(self):
        for value in (-1.1, 1.1):
            with self.assertRaises(ValueError):
                asin_deg(value)

    def test_acos_invalid(self):
        for value in (-1.1, 1.1):
            with self.assertRaises(ValueError):
                acos_deg(value)

    # ------------------ logn -------------------

    def test_logn(self):
        self.assertAlmostEqual(logn(math.e), 1.0)
        self.assertAlmostEqual(logn(1), 0.0)
        self.assertAlmostEqual(logn(math.e**2), 2.0)

    def test_logn_invalid(self):
        with self.assertRaises(ValueError):
            logn(0)

        with self.assertRaises(ValueError):
            logn(-1)

    # ------------------ log10 -------------------

    def test_log10(self):
        self.assertAlmostEqual(log10(1), 0.0)
        self.assertAlmostEqual(log10(10), 1.0)
        self.assertAlmostEqual(log10(1000), 3.0)

    def test_log10_invalid(self):
        with self.assertRaises(ValueError):
            log10(0)

        with self.assertRaises(ValueError):
            log10(-10)

    # ----------------- log2 ----------------

    def test_log2(self):
        self.assertAlmostEqual(log2(1), 0.0)
        self.assertAlmostEqual(log2(2), 1.0)
        self.assertAlmostEqual(log2(1024), 10.0)

    def test_log2_invalid(self):
        with self.assertRaises(ValueError):
            log2(0)

        with self.assertRaises(ValueError):
            log2(-8)

    # ------------------ log ----------------

    def test_log(self):
        self.assertAlmostEqual(log(8, 2), 3.0)
        self.assertAlmostEqual(log(1000, 10), 3.0)
        self.assertAlmostEqual(log(math.e, math.e), 1.0)

    def test_log_invalid_x(self):
        with self.assertRaises(ValueError):
            log(0, 10)

        with self.assertRaises(ValueError):
            log(-5, 10)

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            log(10, 0)

        with self.assertRaises(ValueError):
            log(10, -2)

        with self.assertRaises(ValueError):
            log(10, 1)


if __name__ == "__main__":
    unittest.main(verbosity=2)
