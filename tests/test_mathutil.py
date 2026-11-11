import unittest

from e4demo.mathutil import add, clamp, is_even


class MathUtilTest(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_is_even(self):
        self.assertTrue(is_even(4))
        self.assertFalse(is_even(7))

    def test_clamp_below_range(self):
        self.assertEqual(clamp(0, 1, 10), 1)

    def test_clamp_inside_range(self):
        self.assertEqual(clamp(5, 1, 10), 5)
        self.assertEqual(clamp(1, 1, 10), 1)
        self.assertEqual(clamp(10, 1, 10), 10)
        self.assertEqual(clamp(5, 5, 5), 5)

    def test_clamp_above_range(self):
        self.assertEqual(clamp(11, 1, 10), 10)

    def test_clamp_invalid_range(self):
        with self.assertRaises(ValueError):
            clamp(5, 10, 1)


if __name__ == "__main__":
    unittest.main()
