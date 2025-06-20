# Problem: 739. Daily Temperatures
# Difficulty: Medium
# Date: 2025-05-29

from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        warmer_index = dict()
        cooler_temp_stack = []
        for index, temperature in enumerate(temperatures):
            while cooler_temp_stack and cooler_temp_stack[-1][0] < temperature:
                prev_record = cooler_temp_stack.pop()
                warmer_index[prev_record[1]] = index
            cooler_temp_stack.append((temperature, index))

        res = []
        for i, t in enumerate(temperatures):
            if i in warmer_index:
                res.append(abs(i - warmer_index[i]))
            else:
                res.append(0)
        return res
