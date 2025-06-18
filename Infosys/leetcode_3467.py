
# Problem: 3467. Transform Array
# Difficulty: Easy
# Date: 2025-05-30

from typing import List

class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        l, r = 0, len(nums) - 1
        while l <= r:
            if nums[l] % 2 == 1 and nums[r] % 2 == 0:
                nums[l], nums[r] = nums[l], nums[r]

            elif nums[l] % 2 == 1:
                nums[r] = 1
                r -= 1
                continue
            elif nums[r] % 2 == 0:
                nums[l] = 0
                l += 1
                continue

            nums[l] = 0
            nums[r] = 1
            l += 1
            r -= 1
        return nums