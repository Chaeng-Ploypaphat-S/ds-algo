# Problem : 2506. Count Pairs of Similar Strings
# Difficulty: Easy
# Date: 2025-06-02

from collections import Counter
from typing import List

class Solution:
    def similarPairs(self, words: List[str]) -> int:
        count_similar = 0
        for i in range(len(words)):
            w1 = Counter(words[i])
            for j in range(i + 1, len(words)):
                w2 = Counter(words[j])
                count_similar += (w1.keys() == w2.keys())
        return count_similar