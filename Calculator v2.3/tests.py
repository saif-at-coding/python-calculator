import math
import unittest
from unittest.mock import patch

import operations
import utils


class TestArithmeticOperations(unittest.TestCase):

    def test_add(self):
        self.assertEqual(operations.add(2, 3), 5)
        self.assertEqual(operations.add(-5, 2), -3)
        self.assertEqual(operations.add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(operations.subtract(10, 4), 6)
        self.assertEqual(operations.subtract(4, 10), -6)

    def test_multiply(self):
        self.assertEqual(operations.multiply(5, 6), 30)
        self.assertEqual(operations.multiply(-3, 2), -6)
        self.assertEqual(operations.multiply(0, 100), 0)

    def test_divide(self):
        self.assertEqual(operations.divide(10, 2), 5)
        self.assertEqual(operations.divide(5, 2), 2.5)

    def test_divide_by_zero(self):
        with self.assertRaisesRegex(ZeroDivisionError, "Division by zero not allowed"):
            operations.divide(5, 0)


class TestPowerAndRoots(unittest.TestCase):

    def test_square(self):
        self.assertEqual(operations.square(5), 25)
        self.assertEqual(operations.square(-5), 25)

    def test_cube(self):
        self.assertEqual(operations.cube(3), 27)
        self.assertEqual(operations.cube(-3), -27)

    def test_root(self):
        self.assertEqual(operations.root(25), 5)
        self.assertEqual(operations.root(0), 0)

    def test_root_negative(self):
        with self.assertRaisesRegex(ValueError, "Square root of negatives"):
            operations.root(-1)

    def test_cube_root(self):
        self.assertAlmostEqual(operations.cube_root(27), 3)
        self.assertAlmostEqual(operations.cube_root(-8), -2)

    def test_power(self):
        self.assertEqual(operations.power(2, 10), 1024)
        self.assertEqual(operations.power(2, -3), 0.125)
        self.assertEqual(operations.power(5, 0), 1)

    def test_power_zero_negative(self):
        with self.assertRaisesRegex(
            ZeroDivisionError, "Cannot power zero by negatives"
        ):
            operations.power(0, -2)

    def test_power_negative_fraction(self):
        with self.assertRaisesRegex(ValueError, "imaginary"):
            operations.power(-2, 0.5)


class TestMiscOperations(unittest.TestCase):

    def test_percentage(self):
        self.assertEqual(operations.percentage(50, 200), 25)
        self.assertEqual(operations.percentage(25, 50), 50)

    def test_percentage_zero_base(self):
        with self.assertRaises(ZeroDivisionError):
            operations.percentage(50, 0)

    def test_absolute(self):
        self.assertEqual(operations.absolute(-10), 10)
        self.assertEqual(operations.absolute(10), 10)

    def test_random_generator(self):
        for _ in range(100):
            value = operations.random_int_gen(1, 10)

            self.assertIsInstance(value, int)
            self.assertGreaterEqual(value, 1)
            self.assertLessEqual(value, 10)

    def test_random_generator_invalid(self):
        with self.assertRaisesRegex(ValueError, "Maximum cannot be less than minimum"):
            operations.random_int_gen(10, 1)


class TestTrigonometry(unittest.TestCase):

    def test_sin(self):
        self.assertAlmostEqual(operations.sin_deg(0), 0.0)
        self.assertAlmostEqual(operations.sin_deg(30), 0.5)
        self.assertAlmostEqual(operations.sin_deg(45), math.sqrt(2) / 2)
        self.assertAlmostEqual(operations.sin_deg(90), 1.0)

    def test_cos(self):
        self.assertAlmostEqual(operations.cos_deg(0), 1.0)
        self.assertAlmostEqual(operations.cos_deg(60), 0.5)
        self.assertAlmostEqual(operations.cos_deg(180), -1.0)

    def test_tan(self):
        self.assertAlmostEqual(operations.tan_deg(45), 1.0)
        self.assertAlmostEqual(operations.tan_deg(135), -1.0)

    def test_tan_invalid(self):
        for angle in (90, 270, -90, 450):
            with self.assertRaisesRegex(ValueError, "Undefined"):
                operations.tan_deg(angle)

    def test_asin(self):
        self.assertAlmostEqual(operations.asin_deg(1), 90.0)

    def test_acos(self):
        self.assertAlmostEqual(operations.acos_deg(0), 90.0)

    def test_atan(self):
        self.assertAlmostEqual(operations.atan_deg(1), 45.0)

    def test_inverse_trig_invalid(self):
        for value in (-1.5, 1.5):
            with self.assertRaises(ValueError):
                operations.asin_deg(value)

            with self.assertRaises(ValueError):
                operations.acos_deg(value)


class TestLogarithms(unittest.TestCase):

    def test_logn(self):
        self.assertAlmostEqual(operations.logn(math.e), 1.0)

    def test_log10(self):
        self.assertAlmostEqual(operations.log10(1000), 3.0)

    def test_log2(self):
        self.assertAlmostEqual(operations.log2(1024), 10.0)

    def test_log(self):
        self.assertAlmostEqual(operations.log(8, 2), 3.0)

    def test_invalid_logs(self):

        invalid_values = [0, -1, -10]

        for value in invalid_values:

            with self.assertRaises(ValueError):
                operations.logn(value)

            with self.assertRaises(ValueError):
                operations.log10(value)

            with self.assertRaises(ValueError):
                operations.log2(value)

    def test_invalid_log_base(self):

        invalid_bases = [0, -2, 1]

        for base in invalid_bases:
            with self.assertRaises(ValueError):
                operations.log(10, base)


class TestUtils(unittest.TestCase):

    def setUp(self):
        utils.history.clear()
        utils.HISTORY = ""

    @patch("builtins.print")
    def test_show_menu(self, mock_print):
        utils.show_menu()
        mock_print.assert_called_once()

    def test_add_to_history(self):

        utils.add_to_history("2+2 = 4")

        self.assertEqual(utils.history, ["2+2 = 4"])

    def test_add_empty_history(self):

        utils.add_to_history("")

        self.assertEqual(utils.history, [])

    @patch("builtins.print")
    def test_show_history_empty(self, mock_print):

        utils.show_history()

        mock_print.assert_any_call("No calculation yet, User!")

    @patch("builtins.print")
    def test_show_history(self, mock_print):

        utils.add_to_history("2+2 = 4")
        utils.add_to_history("5*5 = 25")

        utils.show_history()

        mock_print.assert_any_call("Total calculations: 2")

    @patch("builtins.print")
    def test_show_recent(self, mock_print):

        for i in range(10):
            utils.add_to_history(f"Entry {i}")

        utils.show_recent()

        self.assertEqual(len(utils.history[-5:]), 5)

    @patch("builtins.quit")
    @patch("builtins.print")
    def test_user_exit(self, mock_print, mock_quit):

        utils.user_exit()

        mock_print.assert_called_with("Calculator closed by User.")

        mock_quit.assert_called_once()


if __name__ == "__main__":
    unittest.main(verbosity=2)
