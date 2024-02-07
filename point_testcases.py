import point
import unittest


class TestCases(unittest.TestCase):
    def test_Point_1(self):
        point1 = point.Point(7, 20)
        self.assertAlmostEqual(point1.x, 7)
        self.assertAlmostEqual(point1.y, 20)


    def test_Point_2(self):
        point1 = point.Point(4, 19)
        self.assertAlmostEqual(point1.x, 4)
        self.assertAlmostEqual(point1.y, 19)


    def test_Point_eq_1(self):
        point1 = point.Point(1, 20)
        point2 = point.Point(1, 20)
        self.assertEqual(point1, point2)


    def test_Point_eq_2(self):
        point1 = point.Point(1, 20)
        self.assertEqual(point1, point1)


    def test_Point_eq_3(self):
        point1 = point.Point(1, 20)
        point2 = point.Point(2, 20)
        self.assertNotEqual(point1, point2)


    def test_Point_eq_4(self):
        point1 = point.Point(1, 20)
        other = 1.20
        self.assertNotEqual(point1, other)


    def test_Point_repr(self):
        point1 = point.Point(5, 75)
        self.assertEqual(repr(point1p1 ), 'Point(5, 75)')


if __name__ == '__main__':
    unittest.main()
