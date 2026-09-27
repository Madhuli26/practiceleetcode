"""Examples and edge cases for valid_palindrome."""
import unittest
from src.leetcode.valid_palindrome import Solution


class TestSolution(unittest.TestCase):
    def test_case_01(self):
        self.assertEqual(Solution().isPalindrome(*('A man, a plan, a canal: Panama',)), True)

    def test_case_02(self):
        self.assertEqual(Solution().isPalindrome(*('race a car',)), False)

    def test_case_03(self):
        self.assertEqual(Solution().isPalindrome(*(' ',)), True)

    def test_case_04(self):
        self.assertEqual(Solution().isPalindrome(*('',)), True)

    def test_case_05(self):
        self.assertEqual(Solution().isPalindrome(*('0P',)), False)

    def test_case_06(self):
        self.assertEqual(Solution().isPalindrome(*('a.',)), True)
