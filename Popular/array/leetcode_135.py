# Problem: 135. Candy
# Difficulty: Hard
# Date: 2025-06-02

from typing import List

class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candies = [1] * n
        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                if candies[i] <= candies[i - 1]:
                    diff = candies[i - 1] - candies[i]
                    candies[i] += (diff + 1)

        for j in range(n - 2, -1, -1):
            if ratings[j] > ratings[j + 1]:
                if candies[j] <= candies[j + 1]:
                    diff = candies[j + 1] - candies[j]
                    candies[j] += (diff + 1)
        
        return sum(candies)
