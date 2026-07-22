# LeetCode 121 - Best Time to Buy and Sell Stock
"""
Difficulty:
Easy

Pattern:
Greedy / One Pass

Key idea:
- Track the minimum buying price seen so far.
- Calculate the profit if selling at the current price.
- Update the maximum profit during the scan.
- Only keep necessary state instead of checking all buy/sell combinations.

Complexity:
Time: O(n)
Space: O(1)
"""

class Solution:
    def maxProfit(self, prices: list[int]) -> int:

        min_price = prices[0]
        max_profit = 0
        
        for price in prices:
            min_price = min(min_price, price)

            profit = price - min_price

            max_profit = max(max_profit, profit)

        return max_profit