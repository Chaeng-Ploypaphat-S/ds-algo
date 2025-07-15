import math

class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while True:
            seen.add(n)
            chars = [int(char) for char in str(n)]
            nums = [int(math.pow(char, 2)) for char in chars]
            sum_ = sum(nums)
            if sum_ == 1:
                return True
            n = sum_
            if n in seen:
                return False

        return False