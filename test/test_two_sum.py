"""Examples and edge cases for two_sum."""
import unittest
from src.leetcode.two_sum import Solution


class TestSolution(unittest.TestCase):
    def test_case_01(self):
        self.assertEqual(Solution().twoSum(*([2, 7, 11, 15], 9)), [0, 1])

    def test_case_02(self):
        self.assertEqual(Solution().twoSum(*([3, 2, 4], 6)), [1, 2])

    def test_case_03(self):
        self.assertEqual(Solution().twoSum(*([3, 3], 6)), [0, 1])

    def test_case_04(self):
        self.assertEqual(Solution().twoSum(*([-3, 4, 3, 90], 0)), [0, 2])

    def test_case_05(self):
        self.assertEqual(Solution().twoSum(*([0, 4, 3, 0], 0)), [0, 3])

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            Solution().twoSum(*([1, 2], 9))
