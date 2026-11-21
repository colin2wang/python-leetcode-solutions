"""
LeetCode 0088 – Merge Sorted Array

URL: https://leetcode.com/problems/merge-sorted-array/
"""
import pytest


class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        O(m + n) time, O(1) extra space
        """

        i = m - 1
        j = n - 1
        k = m + n - 1

        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1


class TestSolution:
    @pytest.mark.parametrize(
        "nums1, m, nums2, n, expected",
        [
            # Example 1: typical merge with overlapping ranges
            ([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3, [1, 2, 2, 3, 5, 6]),
            # Example 2: equal first elements, nums2 wins the tail
            ([1], 1, [], 0, [1]),
            # Example 3: empty nums1 portion, nums2 fully copied
            ([0], 0, [1], 1, [1]),
            # Edge: nums2 empty, nums1 untouched
            ([4, 5, 6], 3, [], 0, [4, 5, 6]),
            # Edge: single-element arrays, nums2 smaller
            ([2, 0], 1, [1], 1, [1, 2]),
            # Edge: negative and duplicate values
            ([-1, 0, 0, 0], 1, [-1, 2, 3], 3, [-1, -1, 2, 3]),
        ],
    )
    def test_merge(self, nums1, m, nums2, n, expected):
        # NOTE: the Solution.merge body is currently an unimplemented stub;
        # these tests will fail until the implementation is completed.
        # Arrange
        sol = Solution()
        # Act
        result = sol.merge(nums1, m, nums2, n)
        # Assert: merge modifies nums1 in-place and returns None
        assert result is None
        assert nums1 == expected
