# LeetCode 80: Remove Duplicates from Sorted Array II
# Difficulty: Medium
# Date: 2025-07-24

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        curr = 1
        nxt = 2
        while nxt < n:
            if nums[curr] == nums[curr - 1] and nums[curr] == nums[nxt]:

                while nxt < n and nums[curr] == nums[nxt]:
                    nxt += 1
                if nxt >= n:
                    break

            curr += 1
            nums[curr] = nums[nxt]
            nxt += 1

        return curr + 1
        