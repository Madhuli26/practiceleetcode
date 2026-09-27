"""104. Maximum Depth of Binary Tree: number of nodes on the longest root-leaf path.
Iterative DFS: O(n) time, O(h) auxiliary space. Empty tree has depth zero.
"""
from .structures import TreeNode

class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        stack = [(root, 1)] if root else []
        maximum = 0
        while stack:
            node, depth = stack.pop()
            maximum = max(maximum, depth)
            if node.left:
                stack.append((node.left, depth + 1))
            if node.right:
                stack.append((node.right, depth + 1))
        return maximum
