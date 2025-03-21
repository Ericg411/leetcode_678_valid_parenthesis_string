import unittest
from solution import Solution


class TestCheckValidString(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_valid_cases(self):
        self.assertTrue(self.solution.checkValidString("()"))
        self.assertTrue(self.solution.checkValidString("(*)"))
        self.assertTrue(self.solution.checkValidString("(*))"))
        self.assertTrue(self.solution.checkValidString("(())"))
        self.assertTrue(self.solution.checkValidString("(***))"))
        self.assertTrue(self.solution.checkValidString("(********)"))

    def test_invalid_cases(self):
        self.assertFalse(self.solution.checkValidString(")("))
        self.assertFalse(self.solution.checkValidString("((())"))
        self.assertFalse(self.solution.checkValidString("(((***"))
        self.assertFalse(self.solution.checkValidString("(()))"))
        self.assertFalse(self.solution.checkValidString("((*)"))

    def test_edge_cases(self):
        self.assertTrue(self.solution.checkValidString("(*)"))
        self.assertTrue(self.solution.checkValidString("*"))
        self.assertTrue(self.solution.checkValidString(""))
        self.assertFalse(self.solution.checkValidString("("))
        self.assertFalse(self.solution.checkValidString(")"))
        self.assertTrue(self.solution.checkValidString("((*)*"))

if __name__ == "__main__":
    unittest.main()
