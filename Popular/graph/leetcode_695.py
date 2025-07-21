# LeetCode 695 - Max Area of Island
# Difficulty: Medium
# Date: 2025-07-20

from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        rows, cols = len(grid), len(grid[0])

        directions = {(0,1), (0,-1), (1,0), (-1,0)}
        
        max_area = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    area = 0
                    q = [(r, c)]
                    seen = set()
                    while q:
                        curr_r, curr_c = q.pop()
                        if grid[curr_r][curr_c] == 1 and (curr_r, curr_c) not in seen:
                            grid[curr_r][curr_c] = 0
                            area += 1
                            seen.add((curr_r, curr_c))

                            for dr, dc in directions:
                                nr, nc = dr + curr_r, dc + curr_c
                                if nr < 0 or nr == rows or nc < 0 or nc == cols:
                                    continue
                                if grid[nr][nc] == 1:
                                    q.append((nr, nc))

                    max_area = max(max_area, area)

        return max_area