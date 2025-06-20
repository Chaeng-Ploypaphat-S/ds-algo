# LeetCode 2161. Partition Array According to Given Pivot
# Difficulty: Medium
# Date: 2025-06-18

from typing import List

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        lower, equal, higher = [], [], []
        for n in nums:
            if n < pivot:
                lower.append(n)
            elif n > pivot:
                higher.append(n)
            else:
                equal.append(n)
        return lower + equal + higher