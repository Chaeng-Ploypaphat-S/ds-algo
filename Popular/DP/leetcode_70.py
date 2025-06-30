# LeetCode 70: Climbing Stairs
# Difficulty: Easy
# Date: 2025-06-30

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        prev_prev = 1
        prev = 2
        for i in range(3, n + 1):
            curr = prev + prev_prev
            prev_prev = prev
            prev = curr

        return prev