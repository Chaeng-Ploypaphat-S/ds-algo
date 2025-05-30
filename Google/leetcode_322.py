# Problem: 322. Coin Change
# Difficulty: Medium
# Date: 2025-05-16

from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        memo = {}
        
        def compute_num_counts(n):
            if n < 0:
                return float('inf')
            if n == 0:
                return 0
            if n in coins:
                return 1
            if n in memo:
                return memo[n]

            min_coins = float('inf')
            for c in coins:
                min_coins = min(min_coins, compute_num_counts(n-c) + 1)
            
            memo[n] = min_coins
            return memo[n]

        num_coins = compute_num_counts(amount)

        return num_coins if num_coins < float('inf') else -1