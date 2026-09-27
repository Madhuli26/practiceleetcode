"""Examples and edge cases for contains_duplicate."""
import unittest
from src.leetcode.contains_duplicate import Solution


class TestSolution(unittest.TestCase):
    def test_case_01(self):
        self.assertEqual(Solution().containsDuplicate(*([1, 2, 3, 1],)), True)

    def test_case_02(self):
        self.assertEqual(Solution().containsDuplicate(*([1, 2, 3, 4],)), False)

    def test_case_03(self):
        self.assertEqual(Solution().containsDuplicate(*([],)), False)

    def test_case_04(self):
        self.assertEqual(Solution().containsDuplicate(*([1],)), False)

    def test_case_05(self):
        self.assertEqual(Solution().containsDuplicate(*([-1, 0, -1],)), True)
