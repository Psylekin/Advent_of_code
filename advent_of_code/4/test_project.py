import unittest
from project import pysolve

class TestFunctions(unittest.TestCase):

    def test_connection_to_project(self):
        """
        Test if connection is available.
        """
        result = pysolve.connection_test()
        self.assertAlmostEqual(result, 1)


if __name__ == '__main__':
    unittest.main()