"""Examples and edge cases for Group Anagrams."""
import unittest

from src.leetcode.group_anagrams import Solution


class TestGroupAnagrams(unittest.TestCase):
    def test_standard_example(self):
        self.assertEqual(
            Solution().groupAnagrams(['eat', 'tea', 'tan', 'ate', 'nat', 'bat']),
            [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']],
        )

    def test_empty_input(self):
        self.assertEqual(Solution().groupAnagrams([]), [])

    def test_empty_strings(self):
        self.assertEqual(Solution().groupAnagrams(['', 'a', '']), [['', ''], ['a']])

    def test_single_word(self):
        self.assertEqual(Solution().groupAnagrams(['a']), [['a']])

    def test_duplicates_and_character_counts(self):
        self.assertEqual(
            Solution().groupAnagrams(['aab', 'abb', 'aba', 'aab']),
            [['aab', 'aba', 'aab'], ['abb']],
        )

    def test_distinct_words(self):
        self.assertEqual(Solution().groupAnagrams(['a', 'b', 'c']), [['a'], ['b'], ['c']])

    def test_case_sensitive(self):
        self.assertEqual(Solution().groupAnagrams(['Ab', 'bA', 'ab']), [['Ab', 'bA'], ['ab']])

    def test_input_is_not_modified(self):
        words = ['tea', 'eat', 'bat']
        Solution().groupAnagrams(words)
        self.assertEqual(words, ['tea', 'eat', 'bat'])
