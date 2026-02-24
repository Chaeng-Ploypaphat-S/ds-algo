# Problem: 2176. Minimum Number of Pairs in Array
# Difficulty: Easy
# Date: 2025-05-21

from typing import List

class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        set_nums = set(nums)
        if len(set_nums) == len(nums):
            return 0
        
        count = 0
        n = len(nums)

        for i in range(n):
            for j in range(i +1, n):
                if (i * j) % k == 0:
                    if nums[i] == nums[j]:
                        count += 1

        return count