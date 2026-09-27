"""217. Contains Duplicate: determine whether any integer appears more than once.
Hash set: O(n) expected time, O(n) space.
"""
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        return len(set(nums)) != len(nums)
