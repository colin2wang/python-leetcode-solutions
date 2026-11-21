"""
LeetCode 0013 – Roman To Integer

URL: https://leetcode.com/problems/roman-to-integer/
"""
import pytest


class Solution:
    def romanToInt(self, s: str) -> int:
        """
        Convert a Roman numeral string to an integer in one pass.

        Scan left to right: a numeral is subtracted when it is smaller than
        the numeral that follows it (subtractive pairs like IV, CM), and
        added otherwise. Time O(n), space O(1).
        """
        # Symbol values in ascending order
        values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        total = 0
        for i, ch in enumerate(s):
            v = values[ch]
            # Subtractive case: e.g. the I in IV, the C in CM
            if i + 1 < len(s) and v < values[s[i + 1]]:
                total -= v
            else:
                total += v
        return total


@pytest.mark.parametrize("s, expected", [
    # Example 1: single character
    ("III", 3),
    # Example 2: subtractive pair IV
    ("LVIII", 58),
    # Example 3: multiple subtractive pairs
    ("MCMXCIV", 1994),
    # Edge: largest single numeral
    ("M", 1000),
    # Edge: all subtractive combinations
    ("CDXLIV", 444),
    # Edge: maximum value within constraints
    ("MMMCMXCIX", 3999),
    # Edge: four distinct numeral values
    ("DCXXI", 621),
])
def test_solutions(s, expected):
    sol = Solution()
    assert sol.romanToInt(s) == expected