"""
LeetCode 0038 – Count And Say

URL: https://leetcode.com/problems/count-and-say/
"""
import pytest

class Solution:
    def countAndSay(self, n: int) -> str:
        s = "1"                      # 第 1 项
        for _ in range(n - 1):       # 再生成 n-1 项
            nxt = []
            i = 0
            while i < len(s):
                j = i
                while j < len(s) and s[j] == s[i]:
                    j += 1           # j 指向下一段不同字符的起点
                nxt.append(str(j - i))  # 这一段的长度
                nxt.append(s[i])        # 这一段的字符
                i = j
            s = "".join(nxt)
        return s


@pytest.mark.parametrize("x, expected", [
    (1, "1"),
    (2, "11"),
    (3, "21"),
    (4, "1211"),
    (5, "111221"),
    (6, "312211"),
    (7, "13112221"),
    (8, "1113213211"),
    (9, "31131211131221"),
    (10, "13211311123113112211"),
    (11, "11131221133112132113212221"),
    (12, "3113112221232112111312211312113211"),
])
def test_solutions(x, expected):
    sol = Solution()
    assert sol.countAndSay(x) == expected