# Problem: LeetCode 1492. The kth Factor of n
# Difficulty: Medium
# Date: 2025-06-18

class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        curr = 0
        i = 1
        res = []
        while curr <= k and i <= n:
            if n % i == 0:
                curr += 1
                res.append(i)
            if curr == k:
                return i
            i += 1
        return -1