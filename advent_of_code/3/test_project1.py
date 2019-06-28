import unittest
from project1 import pysolve1

class TestFunctions(unittest.TestCase):
    def test_connection_to_project(self):
        """
        Test if connection is available.
        """
        result = pysolve1.connection_test()
        self.assertAlmostEqual(result, 1)

    def test_overlap_counter(self):
        """
        Test if the counter is correct for a simple testcase.
        """
        claims = ["#1 @ 1,3: 4x4", "#2 @ 3,1: 4x4", "#3 @ 5,5: 2x2"]
        result = pysolve1.overlap_counter(claims)
        self.assertEqual(result,4)

    def clear_claim(self):
        """
        Test if the claimes are correctly cleared.
        """
        claim = "#1 @ 1,3: 4x4"
        result = pysolve1.clear_claim(claim)
        self.assertEqual(result,'1,1,3,4,4')

if __name__ == '__main__':
    unittest.main()