"""704. Binary Search: find target in an ascending array of unique integers.
Return -1 when absent. O(log n) time, O(1) space.
"""
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            middle = (left + right) // 2
            if nums[middle] == target:
                return middle
            if nums[middle] < target:
                left = middle + 1
            else:
                right = middle - 1
        return -1
