# Problem : 1455. Check If a Word Occurs As a Prefix of Any Word in a Sentence
# Difficulty: Easy
# Date: 2025-06-06

class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        words = sentence.split()
        for i, word in enumerate(words):
            if word.startswith(searchWord):
                return i + 1
        return -1

        p = 0
        n = len(sentence)
        i = 1
        while p < n:
            if sentence[p] == ' ':
                i += 1
            if sentence[p] == searchWord[0]:
                tmp_p = p
                curr_index = 0
                while tmp_p < n and curr_index < len(searchWord) and sentence[tmp_p] == searchWord[curr_index]:
                    tmp_p += 1
                    curr_index += 1
                if curr_index == len(searchWord):
                    return i
            else:
                p += 1
        return -1