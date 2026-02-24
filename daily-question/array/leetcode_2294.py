# LeetCode 2294. Partition Array Such That Maximum Difference Is K
# Difficulty: Medium
# Date: 2025-06-19

from typing import List

class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        count = 0
        mn = nums[0]
        for num in nums:
            if num - mn > k:
                count += 1
                mn = num
        return count + 1