# LeetCode 2099. Find Subsequence of Length K With the Largest Sum
# Difficulty: Easy
# Date: 2025-06-28

from typing import List

class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        cur_sum = 0
        min_n = float('inf')
        res = []
        for n in nums:
            if len(res) < k:
                res.append(n)
                min_n = min(min_n, n)
                cur_sum += n
            else:
                if n > min_n:
                    i = res.index(min_n)
                    del res[i]
                    res.append(n)
                    min_n = min(res)
                    cur_sum += (n - min_n)
        return res