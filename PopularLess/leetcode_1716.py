# LeetCode 1716. Calculate Money in Leetcode Bank
# Difficulty: Easy
# Date: 2025-07-06

class Solution:
    def totalMoney(self, n: int) -> int:
        sum_ = 0
        curr = 0
        while n > 0:
            if n >= 7:
                local_sum = (curr * 7) + 28
            else:
                local_sum = (curr * n) + int(n * (n + 1) // 2)
            
            sum_ += local_sum
            curr += 1
            n -= 7

        return sum_