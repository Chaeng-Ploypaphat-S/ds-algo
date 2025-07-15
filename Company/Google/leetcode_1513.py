# Problem: 1513. Find the Number of Valid Substrings
# Difficulty: Medium
# Date: 2025-05-24

import math

class Solution:
    def numSub(self, s: str) -> int:
        count_ones = sum([1 if c == '1' else 0 for c in s])

        def get_gauss_sum(n):
            gauss_sum = n * (n + 1) // 2
            return gauss_sum

        res = 0
        p = 0
        n = len(s)
        while p < n:
            if s[p] == '1':
                tmp = p + 1
                while tmp < n and s[tmp] == '1':
                    tmp += 1
                ones = len(s[p:tmp])
                res += get_gauss_sum(ones)
                p = tmp - 1
            p += 1

        return res % (10**9 + 7)