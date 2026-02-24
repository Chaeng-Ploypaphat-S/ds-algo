# LeetCode 2016. Maximum Difference Between Increasing Elements
# Difficulty: Easy
# Date: 2025-06-16

from typing import List

class Solution:
    def maximumDifference(self, nums: List[int]) -> int:

        a = nums[0]
        diff = float('-inf')
        for n in nums[1:]:
            if n > a:
                diff = max(diff, n - a)
            a = min(a, n)

        return diff if diff != float('-inf') else -1