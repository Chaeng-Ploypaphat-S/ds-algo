# Problem: 875. Koko Eating Bananas
# Difficulty: Medium
# Date: 2025-05-26

import math
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        def hours_spent(k):
            hours = 0
            for p in piles:
                hours += math.ceil(p / k)
            return hours
            

        while l < r:
            mid = (l + r) // 2

            actual_h = hours_spent(mid)
            if actual_h > h:
                l = mid + 1
            else:
                r = mid

        return l