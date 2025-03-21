# Problem: 162. Find Peak Element
# Difficulty: Medium
# Date: 2025-03-21

from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        nums = [nums[0] - 1] + nums + [nums[-1] - 1]
        n = len(nums)
        p = 1
        while p < n - 1:
            if nums[p-1] < nums[p] > nums[p+1]:
                return p - 1
            p += 1

        