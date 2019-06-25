import unittest
from project import calc

class TestFunctions(unittest.TestCase):

    def test_no_double_letter(self):
        """
        Test that there are no double letters found if there
        are no double letters.
        """
        result = calc.find_double_and_tribble_chars('abcdef')
        self.assertEqual(result, (0,0))

    def test_one_double_letter(self):
        """
        Test that there are no double letters found if there
        are no double letters.
        """
        result = calc.find_double_and_tribble_chars('bb')
        self.assertEqual(result, (0,0))

    def test_find_unique_characters(self):
        """
        Test, that for a give word you find uniuqe characters.
        """
        result = calc.find_unique_characters('aabb')
        self.assertCountEqual(result, ["a","b"])

if __name__ == '__main__':
    unittest.main()