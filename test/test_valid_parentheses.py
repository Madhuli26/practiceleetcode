"""Examples and edge cases for valid_parentheses."""
import unittest
from src.leetcode.valid_parentheses import Solution


class TestSolution(unittest.TestCase):
    def test_case_01(self):
        self.assertEqual(Solution().isValid(*('()',)), True)

    def test_case_02(self):
        self.assertEqual(Solution().isValid(*('()[]{}',)), True)

    def test_case_03(self):
        self.assertEqual(Solution().isValid(*('{[]}',)), True)

    def test_case_04(self):
        self.assertEqual(Solution().isValid(*('([)]',)), False)

    def test_case_05(self):
        self.assertEqual(Solution().isValid(*(']',)), False)

    def test_case_06(self):
        self.assertEqual(Solution().isValid(*('(',)), False)

    def test_case_07(self):
        self.assertEqual(Solution().isValid(*('',)), True)

    def test_case_08(self):
        self.assertEqual(Solution().isValid(*('a',)), False)
