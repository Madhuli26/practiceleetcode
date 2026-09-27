"""226. Invert Binary Tree: swap left and right children at every node in place.
Iterative DFS: O(n) time, O(h) auxiliary space (h is tree height).
"""
from .structures import TreeNode

class Solution:
    def invertTree(self, root: TreeNode | None) -> TreeNode | None:
        stack = [root] if root else []
        while stack:
            node = stack.pop()
            node.left, node.right = node.right, node.left
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return root
