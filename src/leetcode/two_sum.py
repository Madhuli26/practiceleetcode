"""1. Two Sum: return indices of two values adding to target.
Assumes exactly one answer. Hash map: O(n) time, O(n) space.
"""
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}
        for i, value in enumerate(nums):
            if target - value in seen:
                return [seen[target - value], i]
            seen[value] = i
        raise ValueError("No pair adds to target")
