import math
import unittest

import circle


class CircleTestCase(unittest.TestCase):
    def test_area_positive(self):
        self.assertAlmostEqual(circle.area(2), 4 * math.pi)

    def test_area_zero(self): 
        self.assertEqual(circle.area(0), 0)

    def test_area_negative(self):
        with self.assertRaises(ValueError):
            circle.area(-2)

    def test_perimeter_positive(self):
        self.assertAlmostEqual(circle.perimeter(2), 4 * math.pi)

    def test_perimeter_zero(self):
        self.assertEqual(circle.perimeter(0), 0)


    def test_perimeter_negative(self):
        with self.assertRaises(ValueError):
            circle.perimeter(-2)

    def test_perimeter_negative(self):
        with self.assertRaises(ValueError):
            circle.perimeter(-4)