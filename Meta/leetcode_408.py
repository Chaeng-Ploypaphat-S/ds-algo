# Problem: 408. Valid Word Abbreviation
# Difficulty: Easy
# Date: 2025-03-18

class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        len_w, len_a = len(word), len(abbr)
        w = a = 0
        while w < len_w and a < len_a:
            if not abbr[a].isdigit():
                if word[w] != abbr[a]:
                    return False
                    
                w += 1
                a += 1
            else:
                if abbr[a] == '0':
                    return False
                tmp_a = a
                while tmp_a < len_a and abbr[tmp_a].isdigit():
                    tmp_a += 1

                w += int(''.join(abbr[a:tmp_a]))
                a = tmp_a
                
        return w == len_w and a == len_a
        