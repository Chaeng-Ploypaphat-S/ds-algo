# LeetCode 2200. Find All K-Distant Indices in an Array
# Difficulty: Easy
# Date: 2025-06-23

from typing import List

class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        target = set([j for j, num in enumerate(nums) if num == key])
        res = []
        if target:
            for i, num in enumerate(nums):
                for val in target:
                    if abs(i - val) <= k:
                        res.append(i)
                        break
        return res