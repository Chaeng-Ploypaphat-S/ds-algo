# LeetCode 1475 - Final Prices with a Special Discount in a Shop
# Difficulty: Easy
# Date: 2025-06-10

from typing import List

class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        output = prices[:]
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                if prices[j] <= prices[i]:
                    output[i] -= prices[j]
                    break
        return output