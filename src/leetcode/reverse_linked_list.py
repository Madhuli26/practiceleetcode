"""206. Reverse Linked List: reverse a singly linked list in place.
Iterative pointer reversal: O(n) time, O(1) auxiliary space.
"""
from .structures import ListNode

class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        previous = None
        while head:
            following = head.next
            head.next = previous
            previous, head = head, following
        return previous
