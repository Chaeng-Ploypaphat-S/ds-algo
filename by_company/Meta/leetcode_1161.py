# LeetCode 1161 - Maximum Level Sum of a Binary Tree
# Difficulty: Medium
# Date: 2025-06-01

from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        max_sum = float('-inf')
        level_to_return = 1
        q = deque([(root, 1)])
        
        while q:
            level_size = len(q)
            sum_ = 0
            current_level = None
            for _ in range(level_size):
                node, level = q.popleft()
                if current_level is None:
                    current_level = level
                sum_ += node.val
                if node.left:
                    q.append((node.left, level + 1))
                if node.right:
                    q.append((node.right, level + 1))
            
            if sum_ > max_sum:
                level_to_return = current_level
                max_sum = sum_   

        return level_to_return