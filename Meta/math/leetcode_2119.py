# LeetCode 2119 - A Number After a Double Reversal
# Difficulty: Easy
# Date: 2025-06-13

class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        return num == 0 or num % 10 != 0