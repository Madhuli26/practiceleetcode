"""Examples and edge cases for valid_anagram."""
import unittest
from src.leetcode.valid_anagram import Solution


class TestSolution(unittest.TestCase):
    def test_case_01(self):
        self.assertEqual(Solution().isAnagram(*('anagram', 'nagaram')), True)

    def test_case_02(self):
        self.assertEqual(Solution().isAnagram(*('rat', 'car')), False)

    def test_case_03(self):
        self.assertEqual(Solution().isAnagram(*('a', 'aa')), False)

    def test_case_04(self):
        self.assertEqual(Solution().isAnagram(*('', '')), True)

    def test_case_05(self):
        self.assertEqual(Solution().isAnagram(*('aab', 'abb')), False)
