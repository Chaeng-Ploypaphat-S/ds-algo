# LeetCode 2461. Maximum Subarray Sum After One Operation
# Difficulty: Medium
# Date: 2025-06-20

from collections import Counter
from typing import List

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        curr_sum = sum(nums[:k])
        elmt = Counter(nums[:k])
        mx_sum = curr_sum if len(elmt) == k else None

        for i in range(1, len(nums) - k + 1):
            a = nums[i + k - 1]
            b = nums[i - 1]
            elmt[a] = elmt.get(a, 0) + 1
            elmt[b] -= 1
            if elmt[b] == 0:
                del elmt[b]
            curr_sum += (a - b)
            if len(elmt) == k:
                mx_sum = max(mx_sum, curr_sum) if mx_sum else curr_sum

        return mx_sum if mx_sum else 0