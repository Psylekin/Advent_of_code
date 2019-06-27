import unittest
from project2 import pysolve2

class TestFunctions(unittest.TestCase):
    def test_connection_to_project(self):
        """
        Test if connection is available.
        """
        result = pysolve2.connection_test()
        self.assertAlmostEqual(result, 1)


if __name__ == '__main__':
    unittest.main()