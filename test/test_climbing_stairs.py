"""Examples and edge cases for climbing_stairs."""
import unittest
from src.leetcode.climbing_stairs import Solution


class TestSolution(unittest.TestCase):
    def test_case_01(self):
        self.assertEqual(Solution().climbStairs(*(0,)), 1)

    def test_case_02(self):
        self.assertEqual(Solution().climbStairs(*(1,)), 1)

    def test_case_03(self):
        self.assertEqual(Solution().climbStairs(*(2,)), 2)

    def test_case_04(self):
        self.assertEqual(Solution().climbStairs(*(3,)), 3)

    def test_case_05(self):
        self.assertEqual(Solution().climbStairs(*(5,)), 8)

    def test_case_06(self):
        self.assertEqual(Solution().climbStairs(*(45,)), 1836311903)

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            Solution().climbStairs(*(-1,))
