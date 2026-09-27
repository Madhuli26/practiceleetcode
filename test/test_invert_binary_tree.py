import unittest
from src.leetcode.invert_binary_tree import Solution
from src.leetcode.structures import TreeNode


class TestSolution(unittest.TestCase):
    def test_empty(self):
        self.assertIsNone(Solution().invertTree(None))

    def test_single(self):
        root = TreeNode(1)
        self.assertIs(Solution().invertTree(root), root)
        self.assertEqual(root, TreeNode(1))

    def test_balanced(self):
        root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)),
                        TreeNode(7, TreeNode(6), TreeNode(9)))
        expected = TreeNode(4, TreeNode(7, TreeNode(9), TreeNode(6)),
                            TreeNode(2, TreeNode(3), TreeNode(1)))
        self.assertEqual(Solution().invertTree(root), expected)

    def test_asymmetric(self):
        root = TreeNode(1, TreeNode(2, None, TreeNode(3)))
        self.assertEqual(Solution().invertTree(root),
                         TreeNode(1, None, TreeNode(2, TreeNode(3))))

    def test_double_inversion(self):
        root = TreeNode(1, TreeNode(2), TreeNode(3))
        left, right = root.left, root.right
        Solution().invertTree(Solution().invertTree(root))
        self.assertIs(root.left, left)
        self.assertIs(root.right, right)
