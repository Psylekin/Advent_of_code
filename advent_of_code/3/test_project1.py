import unittest
import pandas as pd
import numpy as np

from project1 import pysolve1

class TestFunctions(unittest.TestCase):
    def test_connection_to_project(self):
        """
        Test if connection is available.
        """
        result = pysolve1.connection_test()
        self.assertAlmostEqual(result, 1)

    def clear_claim(self):
        """
        Test if the claimes are correctly cleared.
        """
        claim = "#1 @ 1,3: 4x4"
        result = pysolve1.clear_claim(claim)
        self.assertEqual(result,'1,1,3,4,4')

    def test_claim_fabric_piece(self):
        """
        Test if the claims claim the correct fabric piece
        """
        claimList = [[1,1,1,3,3],[2,2,2,2,2]]
        fabric = pd.DataFrame(int(0), index=np.arange(1, 6), columns=np.arange(6))
        result = pysolve1.claim_fabric_piece(fabric,claimList)
        target = [[0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 0, 0], [0, 1, 2, 2, 0, 0], [0, 1, 2, 2, 0, 0], [0, 0, 0, 0, 0, 0]]
        self.assertEqual(result.values.tolist(), target)

    def test_count_overlapping_claims(self):
        """
        Test if overlappings are counted correctly
        """
        fabric = pd.DataFrame(int(0), index=np.arange(1, 6), columns=np.arange(6))
        fabric.loc[1,1] = 2
        fabric.loc[1,2] = 5
        result = pysolve1.count_overlapping_claims(fabric)
        self.assertEqual(result, 2)

    def test_find_nonoverlapping_claim(self):
        """
        Test if the finder is correct.
        """
        fabric = pd.DataFrame(int(0), index=np.arange(1, 6), columns=np.arange(6))
        claims = [[1,0,0,2,2],[2,0,0,1,1],[3,4,4,1,1]]
        fabric = pysolve1.claim_fabric_piece(fabric,claims)
        result = pysolve1.find_nonoverlapping_claim(fabric, claims)
        self.assertEqual(result, 3)

if __name__ == '__main__':
    unittest.main()