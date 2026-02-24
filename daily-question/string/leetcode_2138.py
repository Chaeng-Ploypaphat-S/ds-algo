# LeetCode 2138 - Divide a String Into Groups of Size k
# Difficulty: Easy
# Date: 2025-06-21

from typing import List

class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        res = []
        n = len(s)
        p = 0
        while p < n:
            if p + k < n:
                res.append(s[p:p + k])
            else:
                sub_str = s[p:]
                num_char_short = k - len(sub_str)
                sub_str += (fill * num_char_short)
                res.append(sub_str)
            p += k
        return res