"""
LeetCode 0019 – Remove Nth Node From End Of List

URL: https://leetcode.com/problems/remove-nth-node-from-end-of-list/
"""

from typing import Optional

import pytest


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def list_node_to_list(node: Optional[ListNode]) -> Optional[list]:
    """
    Convert a linked list to a Python list for easy comparison.

    Args:
        node: The head node of the linked list

    Returns:
        A Python list containing all values from the linked list, or None if the list is empty
    """
    if node is None:
        return None

    result = []
    while node:
        result.append(node.val)
        node = node.next

    return result

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        Remove the nth node from the end of the linked list.

        Args:
            head: The head node of the linked list
            n: The position from the end (1-based) of the node to remove

        Returns:
            The head of the modified linked list
        """
        dummy = ListNode(0, head)

        # Move fast n steps ahead so slow ends up right before the target node
        fast = dummy
        for _ in range(n):
            fast = fast.next

        slow = dummy
        while fast.next:
            fast = fast.next
            slow = slow.next

        # Skip the target node
        slow.next = slow.next.next

        return dummy.next


@pytest.mark.parametrize("head, n, expected", [
    (ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 2, ListNode(1, ListNode(2, ListNode(3, ListNode(5))))),
    (ListNode(1), 1, None),
    (ListNode(1, ListNode(2)), 1, ListNode(1)),
    (ListNode(1, ListNode(2)), 2, ListNode(2)),
])
def test_solutions(head, n, expected):
    sol = Solution()
    assert list_node_to_list(sol.removeNthFromEnd(head, n)) == list_node_to_list(expected)
