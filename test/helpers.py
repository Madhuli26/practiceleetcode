"""Helpers that detect cycles when inspecting linked-list solutions."""
from src.leetcode.structures import ListNode

def linked(values):
    head = None
    for value in reversed(values):
        head = ListNode(value, head)
    return head

def values(head):
    result, visited = [], set()
    while head is not None:
        if id(head) in visited:
            raise AssertionError("Unexpected cycle in linked list")
        visited.add(id(head))
        result.append(head.val)
        head = head.next
    return result
