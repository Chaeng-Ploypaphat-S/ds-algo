from collections import defaultdict

class Solution:
    def countOddLetters(self, n: int) -> int:
        count_num = defaultdict(int)
        while n > 0:
            curr_digit = int(n % 10)
            count_num[curr_digit] += 1
            n //= 10
        
        char_counts = defaultdict(int)
        def update_char_counts(num_str, frequency):
            for char in num_str:
                char_counts[char] += frequency

        num_map = {
            0: 'zero',
            1: 'one',
            2: 'two',
            3: 'three',
            4: 'four',
            5: 'five',
            6: 'six',
            7: 'seven',
            8: 'eight',
            9: 'nine'
        }

        for number, frequency in count_num.items():
            update_char_counts(num_map[number], frequency)

        count_odd = 0
        for count in char_counts.values():
            if count % 2 == 1:
                count_odd += 1
    
        return count_odd