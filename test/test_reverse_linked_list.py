import unittest
from src.leetcode.reverse_linked_list import Solution
from test.helpers import linked, values


class TestSolution(unittest.TestCase):
    def test_case_01(self):
        heads = [linked(items) for items in ([1, 2, 3, 4, 5],)]
        self.assertEqual(values(Solution().reverseList(*heads)), [5, 4, 3, 2, 1])

    def test_case_02(self):
        heads = [linked(items) for items in ([],)]
        self.assertEqual(values(Solution().reverseList(*heads)), [])

    def test_case_03(self):
        heads = [linked(items) for items in ([1],)]
        self.assertEqual(values(Solution().reverseList(*heads)), [1])

    def test_case_04(self):
        heads = [linked(items) for items in ([1, 2],)]
        self.assertEqual(values(Solution().reverseList(*heads)), [2, 1])

    def test_case_05(self):
        heads = [linked(items) for items in ([1, 1, 2],)]
        self.assertEqual(values(Solution().reverseList(*heads)), [2, 1, 1])
