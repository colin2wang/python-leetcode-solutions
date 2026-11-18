"""
LeetCode 0069 – Sqrtx

URL: https://leetcode.com/problems/sqrtx/
"""
import pytest


class Solution:
    def mySqrt(self, x: int) -> int:
        """
        :type x: int
        :rtype: int
        """
        if x == 0 or x == 1:
            return x

        low, high, res = 1, x, -1

        while low <= high:
            mid = (low + high) // 2
            if mid * mid <= x:
                res = mid
                low = mid + 1
            else:
                high = mid - 1

        return res


@pytest.mark.parametrize("x, expected", [
    (4, 2),
    (8, 2),
    (9, 3),
    (15, 3),
    (16, 4),
    (17, 4),
    (2147395599, 46339),
    (2147483647, 46340)
])
def test_solutions(x, expected):
    sol = Solution()
    assert sol.mySqrt(x) == expected