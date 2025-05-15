# Problem: 2843. Count Symmetric Integers
# Difficulty: Easy
# Date: 2025-05-14

class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        res = 0
        for i in range(max(10, low), high + 1):
            s = str(i)
            if len(s) % 2 == 0:
                half = len(s) // 2
                if sum(map(int, s[:half])) == sum(map(int, s[half:])):
                    res += 1

        return res
        