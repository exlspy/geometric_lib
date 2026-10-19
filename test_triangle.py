import unittest

import triangle


class TriangleTestCase(unittest.TestCase):
    def test_area_positive(self):
        self.assertEqual(triangle.area(2, 1), 1)

    def test_area_zero(self): 
        self.assertEqual(triangle.area(0, 3), 0)

    def test_area_negative(self):
        with self.assertRaises(ValueError):
            triangle.area(-2, 3)


    def test_perimeter_positive(self):
        self.assertEqual(triangle.perimeter(2, 2, 2), 6)

    def test_perimeter_zero(self):
        self.assertEqual(triangle.perimeter(0, 0, 0), 0)


    def test_perimeter_negative(self):
        with self.assertRaises(ValueError):
            triangle.perimeter(-2, 2, 3)