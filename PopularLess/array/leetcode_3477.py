from typing import List

class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        count = len(fruits)
        used = set()
        i = 0
        for f in fruits:
            for i in range(len(baskets)):
                if f <= baskets[i] and i not in used:
                    used.add(i)
                    count -= 1
                    break
        return count