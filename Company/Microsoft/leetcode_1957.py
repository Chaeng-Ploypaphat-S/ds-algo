# Problem: 1957. Delete Characters to Make Fancy String
# Difficulty: Easy
# Date: 2025-03-29

class Solution:
    def makeFancyString(self, s: str) -> str:
        stack = []
        for char in s:
            if len(stack) >= 2 and (stack[-1] == char) and (stack[-2] == char):
                continue
            else:
                stack.append(char)
        return ''.join(stack)
        