# Problem: 2873. Maximum Triplet Value
# Difficulty: Easy
# Date: 2025-05-25

from typing import List

class Solution:
    
    def maximumTripletValue(self, nums: List[int]) -> int:
        mx_sum = float('-inf')
        n = len(nums)

        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    mx_sum = max(mx_sum, (nums[i] - nums[j]) * nums[k])

        return max(0, mx_sum)
    
    def maximumTripletValueOptimized(self, nums: List[int]) -> int:
        n = len(nums)
        mx_sum = float('-inf')
        max_i = nums[0]
        max_j = float('-inf')

        for j in range(1, n):
            max_i = max(max_i, nums[j - 1])
            max_j = max(max_j, nums[j])
            mx_sum = max(mx_sum, (max_i - nums[j]) * max_j)

        return max(0, mx_sum)