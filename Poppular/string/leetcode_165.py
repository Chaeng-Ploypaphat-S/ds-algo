# LeetCode 165. Compare Version Numbers
# Difficulty: Medium
# Date: 2025-06-14


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split('.')
        v2 = version2.split('.')
        p1 = p2 = 0
        
        while p1 < len(v1) and p2 < len(v2):
            num_p1 = int(v1[p1])
            num_p2 = int(v2[p2])
            if num_p1 > num_p2:
                return 1
            if num_p1 < num_p2:
                return -1

            p1 += 1
            p2 += 1

        while p1 < len(v1):
            num_p1 = int(v1[p1])
            if num_p1 > 0:
                return 1
            p1 += 1

        while p2 < len(v2):
            num_p2 = int(v2[p2])
            if num_p2 > 0:
                return -1
            p2 += 1

        return 0