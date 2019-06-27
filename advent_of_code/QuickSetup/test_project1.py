import unittest
from project1 import pysolve1

class TestFunctions(unittest.TestCase):
    def test_connection_to_project(self):
        """
        Test if connection is available.
        """
        result = pysolve1.connection_test()
        self.assertAlmostEqual(result, 1)


if __name__ == '__main__':
    unittest.main()