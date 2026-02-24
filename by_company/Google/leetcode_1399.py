# Problem: 1399. Count Largest Group
# Difficulty: Easy
# Date: 2025-05-13

from collections import defaultdict

class Solution:
    def countLargestGroup(self, n: int) -> int:
        sum_digit_map = defaultdict(list)

        for i in range(1, n + 1):
            sum_digit = sum([int(char) for char in str(i)])
            sum_digit_map[sum_digit].append(i)

        max_length = max(len(lst) for lst in sum_digit_map.values())
        return sum([len(v) == max_length for v in sum_digit_map.values()])
