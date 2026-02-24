# LeetCode 3541. Maximum Frequency Sum of Vowels and Non-Vowels
# Difficulty: Easy
# Date: 2025-07-12

class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels = 'aeiou'
        char_vowels = [0] * 26
        char_not_vowels = [0] * 26
        for char in s:
            char_num = ord(char) - ord('a')
            if char in vowels:
                char_vowels[char_num] += 1
            else:
                char_not_vowels[char_num] += 1

        return max(char_vowels) + max(char_not_vowels)