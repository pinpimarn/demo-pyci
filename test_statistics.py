from unittest import TestCase
from statistics import variance, stdev
from math import sqrt


class StatisticsTest(TestCase):

    def setUp(self):
        self.data1 = [10.0, 10.0, 10.0, 10.0, 10.0]
        self.data2 = [1, 2, 3, 4, 5]
        self.data3 = [10, 2, 8, 4 ,6]

    def test_variance_typical_values(self):
        """variance of typical values"""
        self.assertEqual(0.0, variance(self.data1))
        self.assertEqual(2.0, variance(self.data2))
        self.assertEqual(8.0, variance(self.data3))

    def test_variance_throws_exception(self):
        """variance of an empty list should raise an exception"""
        with self.assertRaises(ValueError):
            var = variance([])

    def test_stdev(self):
        """standard deviation of typical values"""
        self.assertEqual(0.0, stdev(self.data1))
        self.assertEqual(sqrt(2.0), stdev(self.data2))
        self.assertEqual(sqrt(8.0), stdev(self.data3))


if __name__ == '__main__':
    import unittest
    unittest.main(verbosity=1)

