# LeetCode 77. Combinations
# Difficulty: Medium
# Date: 2025-06-02

from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        def backtrack(i=1, curr=[]):
            if len(curr) == k:
                ans.append(curr[:])
                return 
            
            for number in range(i, n + 1):
                if not curr or (curr and number > curr[-1]):
                    curr.append(number)
                    backtrack(number + 1, curr)
                    curr.pop()

        backtrack()
        return ans