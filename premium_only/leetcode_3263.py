# Problem: 3263. Convert Circular Doubly Linked List to Array
# Difficulty: Easy
# Date: 2025-06-03

from typing import List, Optional

class Node:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class Solution:
    def toArray(self, root: 'Optional[Node]') -> List[int]:
        head = root
        res = [root.val]
        curr = root.next
        while curr and curr != head:
            res.append(curr.val)
            curr = curr.next

        return res