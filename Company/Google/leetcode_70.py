# Problem: 70. Climbing Stairs
# Difficulty: Easy
# Date: 2025-05-16

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        prev_prev = 1 # one way to get to 1, which is taking one step
        prev = 2 # 2 ways to get to 2, which is take one 2-step or two 1-step
        for i in range(3, n + 1):
            num_ways_up_to_i = prev + prev_prev
            prev_prev = prev
            prev = num_ways_up_to_i
            
        return prev