# Problem: 496. Next Greater Element I
# Difficulty: Easy
# Date: 2025-05-29


from typing import List

class Solution:
    def safe_index(self, lst, value):
        try:
            return lst.index(value)
        except ValueError:
            return -1

    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums2)
        res = []
        for num in nums1:
            index = self.safe_index(nums2, num)
            if index == -1:
                res.append(-1)
            else:
                p = index
                while p < n and nums2[p] <= num:
                    p += 1
                if p < n:
                    res.append(nums2[p])
                else:
                    res.append(-1)
        return res