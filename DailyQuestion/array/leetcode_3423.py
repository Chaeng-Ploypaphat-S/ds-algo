# LeetCode 3423. Maximum Adjacent Distance
# Difficulty: Easy
# Date: 2025-06-11

from typing import List

class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        max_dist = 0

        for i in range(1, len(nums)):
            max_dist = max(max_dist, abs(nums[i] - nums[i - 1]))

        return max(max_dist, abs(nums[0] - nums[len(nums) - 1]))
        