"""
LeetCode 0122 – Best Time To Buy And Sell Stock Ii

URL: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
"""
import pytest


class Solution:
    def maxProfit(self, prices: list[int]) -> int:

        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]
        return profit


@pytest.mark.parametrize("prices, expected", [
    # Example 1: multiple transactions, profit = (5-1) + (6-3)
    ([7, 1, 5, 3, 6, 4], 7),
    # Example 2: strictly rising, single ride captures all profit
    ([1, 2, 3, 4, 5], 4),
    # Example 3: strictly falling, no profitable transaction
    ([7, 6, 4, 3, 1], 0),
    # Edge: single day, cannot trade
    ([5], 0),
    # Edge: flat prices, no profit
    ([3, 3, 3, 3], 0),
    # Edge: zigzag prices, sell at each local peak
    ([1, 2, 1, 2, 1], 2),
    # Edge: valley after peak, best gains come later
    ([3, 8, 2, 6], 9),
])
def test_solutions(prices, expected):
    # NOTE: the Solution.maxProfit body is currently an unimplemented stub;
    # these tests will fail until the implementation is completed.
    sol = Solution()
    assert sol.maxProfit(prices) == expected