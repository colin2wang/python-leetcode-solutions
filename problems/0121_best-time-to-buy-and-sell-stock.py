"""
LeetCode 0121 – Best Time To Buy And Sell Stock

URL: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
"""
import pytest

class Solution:
    def maxProfit(self, prices: list[int]) -> int:

        min_price = prices[0]
        max_profit = 0
        for price in prices:
            max_profit = max(max_profit, price - min_price)
            min_price = min(min_price, price)
        return max_profit


@pytest.mark.parametrize("prices, expected", [
    # Example 1: buy at 1, sell at 6
    ([7, 1, 5, 3, 6, 4], 5),
    # Example 2: prices only decline, no transaction
    ([7, 6, 4, 3, 1], 0),
    # Edge: single day, cannot trade
    ([5], 0),
    # Edge: two days, rising
    ([1, 2], 1),
    # Edge: two days, falling
    ([2, 1], 0),
    # Edge: valley after a peak, best pair is later
    ([3, 8, 2, 6], 5),
    # Edge: negative prices allowed as values
    ([-3, -1, -2], 2),
])
def test_solutions(prices, expected):
    # NOTE: the Solution.maxProfit body is currently an unimplemented stub;
    # these tests will fail until the implementation is completed.
    sol = Solution()
    assert sol.maxProfit(prices) == expected