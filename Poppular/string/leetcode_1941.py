# LeetCode 1941. Check if All Characters Have Equal Number of Occurrences
# Difficulty: Easy
# Date: 2025-06-18

from collections import Counter

class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        c = Counter(s)
        count = c[s[0]]
        for v in c.values():
            if v != count:
                return False
        return True