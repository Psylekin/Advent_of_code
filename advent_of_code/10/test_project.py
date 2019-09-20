import unittest
from project import pysolve

import re

class TestFunctions(unittest.TestCase):
    def test_connection_to_project(self):
        """
        Test if connection is available.
        """
        result = pysolve.connection_test()
        self.assertAlmostEqual(result, 1)

    def test_transform_input(self):
        """
        Test if input is correct
        """
        input = "position=< 21188,  31669> velocity=<-2, -3>"
        result = pysolve.transform_input(input)
        solution = [21188, 31669, -2 , -3]
        self.assertEqual(result, solution)

if __name__ == '__main__':
    unittest.main()