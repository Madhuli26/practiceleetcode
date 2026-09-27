import unittest
from src.leetcode.merge_two_sorted_lists import Solution
from test.helpers import linked, values


class TestSolution(unittest.TestCase):
    def test_case_01(self):
        heads = [linked(items) for items in ([1, 2, 4], [1, 3, 4])]
        self.assertEqual(values(Solution().mergeTwoLists(*heads)), [1, 1, 2, 3, 4, 4])

    def test_case_02(self):
        heads = [linked(items) for items in ([], [])]
        self.assertEqual(values(Solution().mergeTwoLists(*heads)), [])

    def test_case_03(self):
        heads = [linked(items) for items in ([], [0])]
        self.assertEqual(values(Solution().mergeTwoLists(*heads)), [0])

    def test_case_04(self):
        heads = [linked(items) for items in ([1], [])]
        self.assertEqual(values(Solution().mergeTwoLists(*heads)), [1])

    def test_case_05(self):
        heads = [linked(items) for items in ([-3, -1], [-2, 0])]
        self.assertEqual(values(Solution().mergeTwoLists(*heads)), [-3, -2, -1, 0])

    def test_case_06(self):
        heads = [linked(items) for items in ([1, 1], [1, 1])]
        self.assertEqual(values(Solution().mergeTwoLists(*heads)), [1, 1, 1, 1])
