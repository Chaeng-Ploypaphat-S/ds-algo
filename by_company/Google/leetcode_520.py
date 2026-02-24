# Problem: 520. Detect Capital
# Difficulty: Easy
# Date: 2025-04-03

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        first_is_upper = word[0].isupper()
        the_rest_is_upper = all([char.isupper() for char in word[1:]])
        the_rest_is_lower = all([char.islower() for char in word[1:]])
        
        if first_is_upper:
            return the_rest_is_upper or the_rest_is_lower

        return the_rest_is_lower
        