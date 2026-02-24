# Problem: 2696. Minimum Length of String After Deleting Similar Ends
# Difficulty: Easy
# Date: 2025-03-20

class Solution:
    def minLength(self, s: str) -> int:
        stack = [s[0]]
        for char in s[1:]:
            if char == 'B' and (stack and stack[-1] == 'A'):
                stack.pop()
            elif char == 'D' and (stack and stack[-1] == 'C'):
                stack.pop()
            else:
                stack.append(char)
        return len(stack)