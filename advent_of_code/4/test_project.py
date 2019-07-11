import unittest
import pandas as pd
from project import pysolve

class TestFunctions(unittest.TestCase):

    def test_connection_to_project(self):
        """
        Test if connection is available.
        """
        result = pysolve.connection_test()
        self.assertAlmostEqual(result, 1)

    def test_create_durationSeries(self):
        """
        Test if the durationSeries is created correct.
        """
        #correctSeries = pd.Series([])

        result = pysolve.create_durationSeries(testSleepDf)
        self.assertEqual(result, correctSeries)

if __name__ == '__main__':
    unittest.main()