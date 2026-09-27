"""Examples and edge cases for maximum_subarray."""
import unittest
from src.leetcode.maximum_subarray import Solution


class TestSolution(unittest.TestCase):
    def test_case_01(self):
        self.assertEqual(Solution().maxSubArray(*([-2, 1, -3, 4, -1, 2, 1, -5, 4],)), 6)

    def test_case_02(self):
        self.assertEqual(Solution().maxSubArray(*([1],)), 1)

    def test_case_03(self):
        self.assertEqual(Solution().maxSubArray(*([5, 4, -1, 7, 8],)), 23)

    def test_case_04(self):
        self.assertEqual(Solution().maxSubArray(*([-8, -3, -6, -2, -5],)), -2)

    def test_case_05(self):
        self.assertEqual(Solution().maxSubArray(*([0, 0],)), 0)

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            Solution().maxSubArray(*([] ,))
