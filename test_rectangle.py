import unittest

import rectangle


class RectangleTestCase(unittest.TestCase):
    def test_area_positive(self):
        self.assertEqual(rectangle.area(5, 5), 25)

    def test_area_zero(self): 
        self.assertEqual(rectangle.area(0, 1), 1)

    def test_area_negative(self):
        with self.assertRaises(ValueError):
            rectangle.area(-2, 3)


    def test_perimeter_positive(self):
        self.assertEqual(rectangle.perimeter(2, 2), 8)

    def test_perimeter_zero(self):
        self.assertEqual(rectangle.perimeter(0, 0), 0)


    def test_perimeter_negative(self):
        with self.assertRaises(ValueError):
            rectangle.perimeter(-2, 3)