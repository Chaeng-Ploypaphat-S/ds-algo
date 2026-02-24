# Problem: 516. Longest Palindromic Subsequence
# Difficulty: Medium 
# Date: 2025-05-16

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        s_reversed = s[::-1]
        n = len(s)

        dp = [[0] * (n + 1) for _ in range(n + 1)]

        for r in range(n - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                if s[c] == s_reversed[r]:
                    dp[r][c] = 1 + dp[r + 1][c + 1]
                else:
                    dp[r][c] = max(dp[r + 1][c], dp[r][c + 1])

        return dp[0][0]