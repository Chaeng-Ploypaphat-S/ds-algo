# Problem: 1762. Buildings With an Ocean View
# Difficulty: Medium
# Date: 2025-03-21

from typing import List

class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        
        n = len(heights)
        indices = [n-1]
        p = n - 2
        while p >= 0:
            if heights[p] > heights[indices[-1]]:
                indices.append(p)
            p -= 1

        return indices[::-1]      