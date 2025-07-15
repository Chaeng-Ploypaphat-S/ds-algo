# Problem: 1614. Maximum Nesting Depth of the Parentheses
# Difficulty: Easy
# Date: 2025-03-27

class Solution:
    def maxDepth(self, s: str) -> int:
        max_nesting = 0
        count = 0
        for char in s:
            if char == '(':
                count += 1
            elif char == ')':
                max_nesting = max(max_nesting, count)
                count -= 1
        return max_nesting