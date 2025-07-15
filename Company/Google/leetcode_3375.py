# Problem: 3375. Number of Operations to Make Network Connected
# Difficulty: Easy
# Date: 2025-05-19


from typing import List

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:

        nums = list(set(nums))

        nums.sort()

        if k in nums:
            if nums.index(k) > 0:
                return -1
            return len(nums) - 1

        if k > nums[-1] or k > nums[0]:
            return -1

        return len(nums)