import unittest
from src.leetcode.maximum_depth_of_binary_tree import Solution
from src.leetcode.structures import TreeNode


class TestSolution(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(Solution().maxDepth(None), 0)

    def test_single(self):
        self.assertEqual(Solution().maxDepth(TreeNode(1)), 1)

    def test_balanced(self):
        root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
        self.assertEqual(Solution().maxDepth(root), 3)

    def test_right_branch(self):
        self.assertEqual(Solution().maxDepth(TreeNode(1, None, TreeNode(2))), 2)

    def test_deep_tree(self):
        root = None
        for value in range(2000):
            root = TreeNode(value, root)
        self.assertEqual(Solution().maxDepth(root), 2000)
