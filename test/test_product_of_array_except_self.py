"""Examples and edge cases for product_of_array_except_self."""
import unittest
from src.leetcode.product_of_array_except_self import Solution


class TestSolution(unittest.TestCase):
    def test_case_01(self):
        self.assertEqual(Solution().productExceptSelf(*([1, 2, 3, 4],)), [24, 12, 8, 6])

    def test_case_02(self):
        self.assertEqual(Solution().productExceptSelf(*([-1, 1, 0, -3, 3],)), [0, 0, 9, 0, 0])

    def test_case_03(self):
        self.assertEqual(Solution().productExceptSelf(*([0, 0, 2],)), [0, 0, 0])

    def test_case_04(self):
        self.assertEqual(Solution().productExceptSelf(*([-1, -2, -3],)), [6, 3, 2])

    def test_case_05(self):
        self.assertEqual(Solution().productExceptSelf(*([2, 3],)), [3, 2])
