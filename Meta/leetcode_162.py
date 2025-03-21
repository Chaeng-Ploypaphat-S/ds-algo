# Problem: 162. Find Peak Element
# Difficulty: Medium
# Date: 2025-03-21

from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0

        if nums[-1] > nums[-2]:
            return n - 1

        if nums[0] > nums[1]:
            return 0

        p = 1
        while p < n-1:
            if nums[p-1] < nums[p] > nums[p+1]:
                return p
            p += 1

        