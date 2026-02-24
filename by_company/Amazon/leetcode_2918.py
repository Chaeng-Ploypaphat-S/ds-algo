# Problem: 2918. Minimum Sum of Two Arrays
# Difficulty: Medium
# Date: 2025-05-23

from typing import List

class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        zeros_n1 = nums1.count(0)
        zeros_n2 = nums2.count(0)

        sum_n1 = sum(nums1) + zeros_n1
        sum_n2 = sum(nums2) + zeros_n2

        if zeros_n1 == 0 and sum_n2 > sum_n1:
            return -1

        if zeros_n2 == 0 and sum_n1 > sum_n2:
            return -1

        return max(sum_n1, sum_n2)
    