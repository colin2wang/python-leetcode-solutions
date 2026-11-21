"""
LeetCode 0169 – Majority Element

URL: https://leetcode.com/problems/majority-element/
"""
import pytest

class Solution:
    def majorityElement(self, nums: list[int]) -> int:

        count = 0
        candidate = None
        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if num == candidate else -1
        return candidate


@pytest.mark.parametrize("nums, expected", [
    # Example 1: majority element appears twice out of three
    ([3, 2, 3], 3),
    # Example 2: majority element interleaved with others
    ([2, 2, 1, 1, 1, 2, 2], 2),
    # Edge: single-element array is its own majority
    ([1], 1),
    # Edge: all elements identical
    ([7, 7, 7, 7], 7),
    # Edge: negative values as the majority
    ([-1, -1, 2, -1, 3], -1),
    # Edge: majority element only reaches threshold at the end
    ([1, 2, 1, 2, 1], 1),
])
def test_solutions(nums, expected):
    # NOTE: the Solution.majorityElement body is currently an unimplemented
    # stub; these tests will fail until the implementation is completed.
    sol = Solution()
    assert sol.majorityElement(nums) == expected