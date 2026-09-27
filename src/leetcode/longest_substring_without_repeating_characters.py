"""3. Longest Substring Without Repeating Characters: length of longest unique window.
Sliding window: O(n) time, O(k) space for k distinct characters.
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        left = best = 0
        for right, char in enumerate(s):
            if char in seen:
                left = max(left, seen[char] + 1)
            seen[char] = right
            best = max(best, right - left + 1)
        return best
