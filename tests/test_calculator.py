import unittest

from sample_app.calculator import absolute, add, divide, double, modulo, multiply, negate, power, square, subtract


class CalculatorTests(unittest.TestCase):
    def test_add(self) -> None:
        self.assertEqual(add(2, 3), 5)

    def test_negate(self) -> None:
        self.assertEqual(negate(7), -7)
        self.assertEqual(negate(-4), 4)

    def test_absolute(self) -> None:
        self.assertEqual(absolute(-9), 9)
        self.assertEqual(absolute(5), 5)
        self.assertEqual(absolute(0), 0)

    def test_square(self) -> None:
        self.assertEqual(square(5), 25)
        self.assertEqual(square(-3), 9)
        self.assertEqual(square(0), 0)

    def test_double(self) -> None:
        self.assertEqual(double(6), 12)

    def test_subtract(self) -> None:
        self.assertEqual(subtract(10, 4), 6)

    def test_multiply(self) -> None:
        self.assertEqual(multiply(6, 7), 42)

    def test_divide(self) -> None:
        self.assertEqual(divide(20, 5), 4)

    def test_power(self) -> None:
        self.assertEqual(power(2, 3), 8)

    def test_modulo(self) -> None:
        self.assertEqual(modulo(17, 5), 2)

    def test_modulo_by_zero_raises(self) -> None:
        with self.assertRaises(ValueError):
            modulo(10, 0)

    def test_divide_by_zero_raises(self) -> None:
        with self.assertRaises(ValueError):
            divide(1, 0)


if __name__ == "__main__":
    unittest.main()
