import unittest
from project import pysolve

class TestFunctions(unittest.TestCase):
    def test_connection_to_project(self):
        """
        Test if connection is available.
        """
        result = pysolve.connection_test()
        self.assertAlmostEqual(result, 1)

    def test_find_final_result(self):
        """
        Test if the correct result was found
        """
        result = pysolve.find_final_result()
        self.assertAlmostEqual(result, "3,3")


    def test_calculate_power_level_result_negative(self):
        """
        Test if Powerlevel ist calculated correctly for neg. values
        """
        result = pysolve.calculate_power_level(122,79,57)
        self.assertEqual(result, -5)


    def test_calculate_power_level_result_positive(self):
        """
        Test if Powerlevel ist calculated correctly for positive values
        """
        result = pysolve.calculate_power_level(217,196,39)
        self.assertEqual(result, 0)


    def test_calculate_power_level_result_zero(self):
        """
        Test if Powerlevel ist calculated correctly for 0
        """
        result = pysolve.calculate_power_level(101,153,71)
        self.assertEqual(result, 4)

    def test_create_power_grid_18(self):
        """
        Test if PowerGrid ist calculated correctly for 18
        """
        resultDf = pysolve.create_powerGrid(18)
        result = resultDf.loc[33,45]
        self.assertEqual(result, 4)

    def test_create_power_grid_42(self):
        """
        Test if PowerGrid ist calculated correctly for 18
        """
        resultDf = pysolve.create_powerGrid(42)
        result = resultDf.loc[21,61]
        self.assertEqual(result, 4)

    def calculate_gridPower(self):
        nrList = [x for x in range(1,4)]
        dataFrame = pd.DataFrame(index = nrList, columns = nrList, 1)
        result = calculate_gridPower(dataFrame)
        self.assertEqual(result, 9)

if __name__ == '__main__':
    unittest.main()