# Problem: 2303. Calculate Tax
# Difficulty: Easy
# Date: 2025-04-11

from typing import List

class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        n = len(brackets)
        prev = 0
        i = 0
        tax = 0
        untaxed_income = income
        for i in range(n):
            if untaxed_income > 0:
                u, p = brackets[i][0], brackets[i][1]
                tax += (min(u, income) - prev) * p / 100
                untaxed_income -= (u-prev)
                prev = u
            
        return tax
