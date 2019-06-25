import unittest
from project2 import calc2

class TestFunctions(unittest.TestCase):

    def test_no_double_letter(self):
        """
        Test that there are no double letters found if there
        are no double letters.
        """
        result = calc2.hello()
        self.assertEqual(result, 1)

    def count_differences(self):
        """
        Test if 1 differences works.
        """
        result = calc2.count_differences("asdf", "asdg")
        self.assertEqual(result, 2)



if __name__ == '__main__':
    unittest.main()