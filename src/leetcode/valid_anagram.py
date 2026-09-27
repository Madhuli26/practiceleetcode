"""242. Valid Anagram: determine whether strings contain the same character counts.
Frequency counting: O(n+m) time, O(k) space for k distinct characters.
"""
from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
