# Problem: 1346. Check If N and Its Double Exist
# Difficulty: Easy
# Date: 2025-03-17

from collections import Counter
from typing import List

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        c = Counter(arr)
        for k in c.keys():
            if k != 0 and k * 2 in c:
                return True
            if k == 0 and c[0] > 1:
                return True
        return False