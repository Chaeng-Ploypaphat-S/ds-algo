# LeetCode 3498. Reverse Degree of a String
# Difficulty: Easy
# Date: 2025-06-09

class Solution:
    def reverseDegree(self, s: str) -> int:
        sum_ = 0
        for i, char in enumerate(s):
            ir = 26 - (ord(char) - ord('a'))
            sum_ += ir * (i + 1)
        return sum_