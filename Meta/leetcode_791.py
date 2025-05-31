# Problem: 791. Custom Sort String
# Difficulty: Medium
# Date: 2025-05-30

from collections import Counter

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        counter_s = Counter(s)
        res = []
        for char in order:
            if char not in counter_s:
                continue
            num_chars = counter_s[char]
            res.append(char * num_chars)
            del counter_s[char]
                
        for char, count in counter_s.items():
            res.append(char * count)
            
        return ''.join(res)