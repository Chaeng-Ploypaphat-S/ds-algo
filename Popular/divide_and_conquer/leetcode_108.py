# LeetCode 108: Convert Sorted Array to Binary Search Tree
# Difficulty: Easy
# Date: 2025-06-08

from typing import List, Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return 

        n = len(nums)
        created = set()
        def helper(start, end):
            i = (start + end) // 2
            if i < 0 or i >= n or i in created:
                return None
            created.add(i)
            node = TreeNode(nums[i])
            node.left = helper(start, i)
            node.right = helper(i + 1, end)
            return node

        return helper(0, n-1)
    