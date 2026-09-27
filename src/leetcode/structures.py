"""Shared LeetCode-compatible linked-list and binary-tree nodes."""
from __future__ import annotations
from dataclasses import dataclass

@dataclass
class ListNode:
    val: int = 0
    next: ListNode | None = None

@dataclass
class TreeNode:
    val: int = 0
    left: TreeNode | None = None
    right: TreeNode | None = None
