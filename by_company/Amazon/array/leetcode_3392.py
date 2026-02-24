# LeetCode 3392. Count Subarrays with Equal Average
# Difficulty: Easy
# Date: 2025-06-15

from typing import List

class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        count = 0
        n = len(nums)
        for i in range(n - 2):
            if nums[i + 1] % 2 == 0:
                if (nums[i] + nums[i + 2]) * 2 == nums[i + 1]:
                    count += 1
        return count