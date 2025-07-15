# Problem: 999. Available Captures for Rook
# Difficulty: Easy
# Date: 2025-05-13

from typing import List

class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        
        def collect_pawns(i, j):
            count_pawns = 0
            for del_i, del_j in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                pos_i, pos_j = i + del_i, j + del_j
                while 0 <= pos_i < 8 and 0 <= pos_j < 8:
                    if board[pos_i][pos_j] == 'B':
                        break
                    if board[pos_i][pos_j] == 'p':
                        count_pawns += 1
                        break
                    pos_i, pos_j = pos_i + del_i, pos_j + del_j
            return count_pawns             
        
        for i in range(8):
            for j in range(8):
                if board[i][j] == 'R':
                    return collect_pawns(i, j)
