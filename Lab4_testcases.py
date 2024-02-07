# Your Name: Berfredd Quezon
# Your Section: 11

import point
import Lab4
import unittest


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Task 1
    def test_first_element_1(self):
        input = [[1,2], [3,4]]
        result = Lab4.first_element(input)
        expected = [1, 3]
        self.assertEqual(expected, result)


    def test_first_element_2(self):
        input = [[5,3],[4,-2],[],[3,1],[2,100],[1,-2041]]
        result = Lab4.first_element(input)
        expected = [5,4,3,2,1]
        self.assertEqual(expected, result)


    # Task 2
    def test_x_coordinates_1(self):
        P1 = point.Point(3, -8)
        P2 = point.Point(4,1)
        input = [P1,P2]
        result = Lab4.x_coordinates(input)
        expected = [3,4]
        self.assertEqual(expected,result)

    def test_x_coordinates_2(self):
        input = []
        result = Lab4.x_coordinates(input)
        expected = None
        self.assertEqual(expected,result)


    # Task 3
    def test_are_in_positive_quadrant_1(self):
        P1 = point.Point(4.2,-2.8)
        P2 = point.Point(2.0,7.1)
        P3 = point.Point(6.6,1.4)
        input = [P1,P2,P3]
        result = Lab4.are_in_positive_quadrant(input)
        expected = [P2,P3]
        self.assertEqual(expected,result)

    def test_are_in_positive_quadrant_2(self):
        input = []
        result = Lab4.are_in_positive_quadrant(input)
        expected = None
        self.assertEqual(expected,result)


    # Task 4
    def test_euclidean_distance_1(self):
        point1 = point.Point(3,4)
        point2 = point.Point(5,2)
        result = Lab4.euclidean_distance(point1,point2)
        expected = 2.828
        self.assertAlmostEqual(expected,result,3)

    def test_euclidean_distance_2(self):
        point1 = point.Point(-10,-12)
        point2 = point.Point(48,-3)
        result = Lab4.euclidean_distance(point1,point2)
        expected = 58.69
        self.assertAlmostEqual(expected,result,2)


    # Task 5
    def test_manhattan_distance_1(self):
        point1 = point.Point(25, 2)
        point2 = point.Point(33, -10)
        result = Lab4.manhattan_distance(point1,point2)
        expected = 20.00000
        self.assertAlmostEqual(expected,result,5)

    def test_manhattan_distance_2(self):
        point1 = point.Point(1, -5)
        point2 = point.Point(3, -7)
        result = Lab4.manhattan_distance(point1,point2)
        expected = 4.0
        self.assertAlmostEqual(expected,result,1)


    # Task 6
    def test_distance_all_1(self):
        input = []
        result = Lab4.distance_all(input)
        expected = None
        self.assertEqual(expected,result)

    def test_distance_all_2(self):
        point1 = point.Point(4,9)
        point2 = point.Point(-2, -6)
        point3 = point.Point(-5,7)
        point4 = point.Point(0,0)
        input = [point1, point2, point3, point4]
        result = Lab4.distance_all(input)
        expected = [9.849,6.325,8.602,0.0]
        self.assertEqual(expected,result)


if __name__ == '__main__':
    unittest.main()
