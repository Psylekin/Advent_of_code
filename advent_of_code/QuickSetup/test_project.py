import unittest
from project import pysolve

class TestFunctions(unittest.TestCase):
    def test_connection_to_project(self):
        """
        Test if connection is available.
        """
        result = pysolve.connection_test()
        self.assertAlmostEqual(result, 1)

    def test_solve_riddle_1(self):
        """
        Test if the riddle is correctly solved.
        """
        result = pysolve.solve_riddle_1()
        self.assertEqual(result, "CABDFE")

if __name__ == '__main__':
    unittest.main()