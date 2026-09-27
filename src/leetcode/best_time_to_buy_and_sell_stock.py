"""121. Best Time to Buy and Sell Stock: maximum profit from one buy then sell.
Running minimum: O(n) time, O(1) space. No profitable trade returns zero.
"""
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        minimum, profit = float('inf'), 0
        for price in prices:
            minimum = min(minimum, price)
            profit = max(profit, price - minimum)
        return profit
