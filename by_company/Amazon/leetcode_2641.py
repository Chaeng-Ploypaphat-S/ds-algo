
# Problem: 2641. Cousins in Binary Tree II
# Difficulty: Medium
# Date: 2025-05-11

from collections import defaultdict
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        level_sum = defaultdict(int)

        def compute_sum_level(node, level):
            if not node:
                return
            if level > 1:
                level_sum[level] += node.val

            compute_sum_level(node.left, level + 1)
            compute_sum_level(node.right, level + 1)

        compute_sum_level(root, 0)

        def dfs(node, level):
            if not node:
                return

            if level < 2:
                node.val = 0

            if not node.left and not node.right:
                return
            
            val = level_sum[level + 1]
            if node.left and node.right:
                node.right.val = node.left.val = val - (node.left.val + node.right.val)
            elif node.left:
                node.left.val = val - node.left.val
            else:
                node.right.val = val - node.right.val

            dfs(node.left, level + 1)
            dfs(node.right, level + 1)

        dfs(root, 0)

        return root