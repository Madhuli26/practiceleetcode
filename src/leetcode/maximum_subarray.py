"""53. Maximum Subarray: largest sum of a nonempty contiguous subarray.
Kadane's algorithm: O(n) time, O(1) space. Input must be nonempty.
"""
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        if not nums:
            raise ValueError("nums must be nonempty")
        current = best = nums[0]
        for i in range(1, len(nums)):
            current = max(nums[i], current + nums[i])
            best = max(best, current)
        return best
