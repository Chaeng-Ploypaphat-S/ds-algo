# LeetCode 2379 - Minimum Recolors to Get K Consecutive Black Blocks
# Difficulty: Easy
# Date: 2025-06-05

class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:

        curr_white = sum([char == 'W' for char in blocks[:k]])
        min_white = curr_white
        
        for i in range(1, len(blocks) - k + 1):
            curr_white -= (blocks[i - 1] == 'W')
            curr_white += (blocks[i + k - 1] == 'W')
            min_white = min(min_white, curr_white)

        return min_white