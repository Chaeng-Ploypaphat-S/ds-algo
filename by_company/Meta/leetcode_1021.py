# Problem: 1021. Remove Outermost Parentheses
# Difficulty: Easy
# Date: 2025-03-13

class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res = ""
        n = len(s)
        stack = []
        start = 0
        p = 0
        while p < n:
            if s[p] == ')':
                stack.pop()
                if not stack:
                    res += s[start+1:p]
                    start = p + 1
            else:
                stack.append(s[p])
            p += 1
        return res