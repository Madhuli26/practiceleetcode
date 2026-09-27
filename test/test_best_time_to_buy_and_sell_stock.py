"""Examples and edge cases for best_time_to_buy_and_sell_stock."""
import unittest
from src.leetcode.best_time_to_buy_and_sell_stock import Solution


class TestSolution(unittest.TestCase):
    def test_case_01(self):
        self.assertEqual(Solution().maxProfit(*([7, 1, 5, 3, 6, 4],)), 5)

    def test_case_02(self):
        self.assertEqual(Solution().maxProfit(*([7, 6, 4, 3, 1],)), 0)

    def test_case_03(self):
        self.assertEqual(Solution().maxProfit(*([2],)), 0)

    def test_case_04(self):
        self.assertEqual(Solution().maxProfit(*([],)), 0)

    def test_case_05(self):
        self.assertEqual(Solution().maxProfit(*([2, 2, 2],)), 0)

    def test_case_06(self):
        self.assertEqual(Solution().maxProfit(*([1, 2, 3, 4],)), 3)
