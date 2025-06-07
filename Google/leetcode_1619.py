# LeetCode 1619. Mean of Array After Removing Some Elements
# Difficulty: Easy
# Date: 2025-06-07

from typing import List

class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()
        num_to_remove = int(len(arr) * .05)
        a = arr[num_to_remove:-num_to_remove]
        return sum(a) / len(a)