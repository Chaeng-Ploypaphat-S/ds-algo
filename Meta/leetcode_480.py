# Problem: 480. Sliding Window Median
# Difficulty: Hard
# Date: 2025-03-15

import bisect
from typing import List

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        
        half = k // 2
        def get_median(arr):
            if k % 2 == 0:
                return (arr[half-1] + arr[half]) / 2
            else:
                return arr[half]
        
        arr = sorted(nums[:k])
        medians = [get_median(arr)]
        n = len(nums)
        for i in range(1, n-k+1):
            arr.pop(bisect.bisect_left(arr, nums[i - 1]))
            bisect.insort_left(arr, nums[i+k-1])
            medians.append(get_median(arr))

        return medians