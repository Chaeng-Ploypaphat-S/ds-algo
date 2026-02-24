# LeetCode 2451. Odd String Difference
# Difficulty: Easy
# Date: 2025-06-20

from typing import List

class Solution:
    def oddString(self, words: List[str]) -> str:

        def compute(w):
            arr = []
            for j in range(len(w) - 1):
                arr.append(ord(w[j + 1]) - ord(w[j]))
            return tuple(arr)

        p1 = compute(words[0])
        p2 = compute(words[1])
        for w in words[2:]:
            p = compute(w)
            if p == p1 and p != p2:
                return words[1]
            if p != p1 and p == p2:
                return words[0]
            if p != p1 and p1 == p2:
                return w