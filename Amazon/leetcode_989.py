# Problem: 989. Add to Array-Form of Integer
# Difficulty: Easy
# Date: 2025-05-04

from typing import List

class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        cur = 0
        for n in num:
            cur *= 10
            cur += n
        cur += k
        ans = []
        while cur:
            cur, mod = divmod(cur, 10)
            ans.append(mod)
        ans.reverse()
        return ans