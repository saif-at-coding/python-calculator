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


if __name__ == "__main__":
    unittest.main(verbosity=2)

# I am new to tests so I asked chatgpt to create one for me :)
