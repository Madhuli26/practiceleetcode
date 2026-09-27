"""70. Climbing Stairs: count ways to climb n stairs with steps of size 1 or 2.
Rolling dynamic programming: O(n) time, O(1) space. n must be nonnegative.
"""
class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 0:
            raise ValueError("n must be nonnegative")
        previous, current = 1, 1
        for _ in range(n):
            previous, current = current, previous + current
        return previous
