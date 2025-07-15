# Problem: 1678. Goal Parser Interpretation
# Difficulty: Easy
# Date: 2025-04-01


class Solution:
    def interpret(self, command: str) -> str:
        n = len(command)
        res = []
        pos = 0
        while pos < n:
            char = command[pos]
            if char  == '(':
                if command[pos+1] == ')':
                    res.append('o')
                    pos += 1
                else:
                    res.append('al')
                    pos += 3
            else:
                res.append(char)
            pos += 1

        return ''.join(res)