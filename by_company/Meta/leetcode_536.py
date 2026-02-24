# Problem: 536. Construct Binary Tree from String
# Difficulty: Medium
# Date: 2025-03-12

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def str2tree(self, s: str) -> Optional[TreeNode]:
        return self.str2tree_helper(s)

    def str2tree_helper(self, s):
        if not s:
            return
        n = len(s)
        end_root = 0
        while end_root < n and s[end_root] != '(':
            end_root += 1
        root_val = int(s[:end_root])

        root = TreeNode(val=root_val)

        # if there is a child or children, add it or them to the root.
        end_left = None
        if end_root < n:
            count_map = {')': -1, '(': 1}
            pair_count = 0
            end_left = end_root
            while end_left < n:
                pair_count += count_map.get(s[end_left], 0)
                if pair_count == 0:
                    break
                end_left += 1

            root.left = self.str2tree_helper(s[end_root+1:end_left])
            
        # if there is a right node, add it to the root. 
        if end_left and end_left + 1 < n:
            root.right = self.str2tree_helper(s[end_left+2:-1])
            
        return root
        