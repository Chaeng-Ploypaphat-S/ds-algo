# LeetCode 2657. Find the Prefix Common Array of Two Arrays
# Difficulty: Medium
# Date: 2025-06-12

from typing import List

class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        set_a = set()
        set_b = set()
        res = []
        for i in range(len(A)):
            set_a.add(A[i])
            set_b.add(B[i])
            intersect = set_a.intersection(set_b)
            res.append(len(intersect))
        return res
            