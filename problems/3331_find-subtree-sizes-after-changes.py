"""
LeetCode 3331 – Find Subtree Sizes After Changes

URL: https://leetcode.com/problems/find-subtree-sizes-after-changes/
"""
from typing import List

import pytest

class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)
        children = [[] for _ in range(n)]
        root = 0
        ord_a = ord('a')
        for i, p in enumerate(parent):
            if p == -1:
                root = i
            else:
                children[p].append(i)

        new_children = [[] for _ in range(n)]
        char_anc = [-1] * 26
        stack = [root]
        prev_stk = []

        while stack:
            node = stack.pop()
            if node < 0:
                # leave
                node = -node - 1
                c_idx = ord(s[node]) - ord_a
                char_anc[c_idx] = prev_stk.pop()
                continue

            c_idx = ord(s[node]) - ord_a
            prev = char_anc[c_idx]
            char_anc[c_idx] = node
            prev_stk.append(prev)
            stack.append(-node - 1)
            for child in children[node]:
                cc = ord(s[child]) - ord_a
                target = char_anc[cc] if char_anc[cc] != -1 else node
                new_children[target].append(child)
                stack.append(child)

        size = [1] * n
        stack = [root]
        while stack:
            u = stack.pop()
            if u >= 0:
                stack.append(-u - 1)
                for v in reversed(new_children[u]):
                    stack.append(v)
            else:
                u = -u - 1
                for v in new_children[u]:
                    size[u] += size[v]
        return size

@pytest.mark.parametrize("parent, s, expected", [
    # Example 1: nodes reconnect to the nearest same-char ancestor
    ([-1, 0, 0, 1, 1, 1], "abaabc", [6, 3, 1, 1, 1, 1]),
    # Example 2: mixed subtree sizes after changes
    ([-1, 0, 4, 0, 1], "abbba", [5, 2, 1, 1, 1]),
    # Edge: single node tree
    ([-1], "a", [1]),
    # Edge: chain where every node has the same char, tree stays a chain
    ([-1, 0, 1], "aaa", [3, 2, 1]),
    # Edge: all chars distinct, no reconnects happen
    ([-1, 0, 0], "abc", [3, 1, 1]),
])
def test_solutions(parent, s, expected):
    sol = Solution()
    assert sol.findSubtreeSizes(parent, s) == expected