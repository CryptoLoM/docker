import unittest

from Docker.main import circle_area
from Docker.main import pi

class TestCircleArea(unittest.TestCase):

    def test_area(self):
        self.assertEqual(circle_area(3), pi*3**2)
        self.assertEqual(circle_area(2.5), pi*2.5**2)
        self.assertEqual(circle_area(1), pi*1**2)
        self.assertEqual(circle_area(0), pi*0**2)

    def test_vales(self):
        self.assertRaises(ValueError, circle_area, -1)
        self.assertRaises(ValueError, circle_area, -2)

    def test_types(self):
        self.assertRaises(TypeError, circle_area, False)
        self.assertRaises(TypeError, circle_area, 2j)
        self.assertRaises(TypeError, circle_area, [1,2,8])
        self.assertRaises(TypeError, circle_area, 'Dimasik give a max point pls')
        self.assertRaises(TypeError, circle_area, 'eight')

