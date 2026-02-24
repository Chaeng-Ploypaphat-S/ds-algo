
# Problem: 270. Closest Binary Search Tree Value
# Difficulty: Easy
# Date: 2025-05-26

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        
        def dfs(node):
            if not node:
                return float('inf'), float('inf')

            l_diff, l_val = dfs(node.left)
            r_diff, r_val = dfs(node.right)

            curr_diff = abs(target - node.val)

            if l_diff <= curr_diff and l_diff < r_diff:
                return l_diff, l_val

            if r_diff < curr_diff and r_diff < l_diff:
                return r_diff, r_val

            if curr_diff < l_diff and curr_diff <= r_diff:
                return curr_diff, node.val


        _, node_val = dfs(root)
        return node_val