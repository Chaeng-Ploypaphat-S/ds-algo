# Problem: 2570. Merge Two 2D Arrays by Summing Values
# Difficulty: Easy
# Date: 2025-03-12

from types import List

class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        res = []
        m, n = len(nums1), len(nums2)
        p1 = p2 = 0
        while p1 < m and p2 < n:
            if nums1[p1][0] < nums2[p2][0]:
                res.append(nums1[p1])
                p1 += 1
            elif nums1[p1][0] > nums2[p2][0]:
                res.append(nums2[p2])
                p2 += 1
            else:
                merged_value = [nums1[p1][0], nums1[p1][1]+nums2[p2][1]]
                res.append(merged_value)
                p1 += 1
                p2 += 1
        
        if p1 < m:
            while p1 < m:
                res.append(nums1[p1])
                p1 += 1
        
        if p2 < n:
            while p2 < n:
                res.append(nums2[p2])
                p2 += 1
        
        return res