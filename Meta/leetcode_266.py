# Problem: 266. Palindrome Permutation
# Difficulty: Easy
# Date: 2025-05-16


from collections import Counter

class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        count_s = Counter(s)
        num_odd = 0
        for v in count_s.values():
            if v % 2 == 1:
                num_odd += 1
            if num_odd > 1:
                return False
        return True