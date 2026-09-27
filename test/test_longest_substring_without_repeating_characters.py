"""Examples and edge cases for longest_substring_without_repeating_characters."""
import unittest
from src.leetcode.longest_substring_without_repeating_characters import Solution


class TestSolution(unittest.TestCase):
    def test_case_01(self):
        self.assertEqual(Solution().lengthOfLongestSubstring(*('abcabcbb',)), 3)

    def test_case_02(self):
        self.assertEqual(Solution().lengthOfLongestSubstring(*('bbbbb',)), 1)

    def test_case_03(self):
        self.assertEqual(Solution().lengthOfLongestSubstring(*('pwwkew',)), 3)

    def test_case_04(self):
        self.assertEqual(Solution().lengthOfLongestSubstring(*('',)), 0)

    def test_case_05(self):
        self.assertEqual(Solution().lengthOfLongestSubstring(*('abba',)), 2)

    def test_case_06(self):
        self.assertEqual(Solution().lengthOfLongestSubstring(*('dvdf',)), 3)

    def test_case_07(self):
        self.assertEqual(Solution().lengthOfLongestSubstring(*(' ',)), 1)
