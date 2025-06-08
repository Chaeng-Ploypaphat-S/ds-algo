# LeetCode 1861 - Rotating the Box
# Difficulty: Medium
# Date: 2025-06-07

from typing import List

class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        # 1. Rotate
        rows = len(boxGrid)
        cols = len(boxGrid[0])
        output = [["."] * rows for _ in range(cols)]
        
        for r in range(len(boxGrid)):
            for c in range(len(boxGrid[0])):
                output[c][rows - r - 1] = boxGrid[r][c]

        # 2. Drop
        rows_output = len(output)
        seen = set()
        for i in range(len(output) - 1, -1, -1):
            for j in range(len(output[0])):
                if output[i][j] == '#':
                    tmp_i = i + 1
                    if tmp_i < rows_output and (output[tmp_i][j] != '#' and output[tmp_i][j] != '*'):
                        while tmp_i < rows_output and output[tmp_i][j] == '.':
                            tmp_i += 1
                        tmp_i -= 1
                        if tmp_i < rows_output and (tmp_i, j) not in seen:
                            output[tmp_i][j] = '#'
                            output[i][j] = '.'
                            seen.add((tmp_i, j))
        return output