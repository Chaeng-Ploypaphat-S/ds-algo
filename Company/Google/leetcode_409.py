# Problem: 409. Longest Palindrome
# Difficulty: Easy
# Date: 2025-04-02

from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        count_map = Counter(s)
        palindrome_len = 0
        count_single = 0
        for k, v in count_map.items():
            if v % 2 != 0:
                count_single = 1
            num_char = v // 2
            palindrome_len += num_char
        return (palindrome_len * 2) + count_single
        