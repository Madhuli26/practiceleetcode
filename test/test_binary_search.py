"""Examples and edge cases for binary_search."""
import unittest
from src.leetcode.binary_search import Solution


class TestSolution(unittest.TestCase):
    def test_case_01(self):
        self.assertEqual(Solution().search(*([-1, 0, 3, 5, 9, 12], 9)), 4)

    def test_case_02(self):
        self.assertEqual(Solution().search(*([-1, 0, 3, 5, 9, 12], 2)), -1)

    def test_case_03(self):
        self.assertEqual(Solution().search(*([1], 1)), 0)

    def test_case_04(self):
        self.assertEqual(Solution().search(*([], 1)), -1)

    def test_case_05(self):
        self.assertEqual(Solution().search(*([1, 2, 3], 1)), 0)

    def test_case_06(self):
        self.assertEqual(Solution().search(*([1, 2, 3], 3)), 2)

    def test_case_07(self):
        self.assertEqual(Solution().search(*([1], 0)), -1)
