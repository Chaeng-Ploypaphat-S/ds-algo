# LeetCode 245. Shortest Word Distance III
# Difficulty: Medium
# Date: 2025-06-17

from typing import List

class Solution:
    def shortestWordDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        dist = float('inf')
        i1 = i2 = None
        same = word1 == word2

        for i, word in enumerate(wordsDict):
            if word == word1:
                if same:
                    i1 = i2
                    i2 = i
                else:
                    i1 = i
            elif word == word2:
                i2 = i

            if i1 is not None and i2 is not None:
                dist = min(dist, abs(i1 - i2))

        return dist