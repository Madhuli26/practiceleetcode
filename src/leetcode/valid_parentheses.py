"""20. Valid Parentheses: check balanced (), [], and {} brackets.
Stack: O(n) time, O(n) space. Non-bracket characters are invalid.
"""
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')': '(', ']': '[', '}': '{'}
        for char in s:
            if char in '([{':
                stack.append(char)
            elif char not in pairs or not stack or stack.pop() != pairs[char]:
                return False
        return not stack
