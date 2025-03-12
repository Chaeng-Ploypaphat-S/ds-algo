# Problem: 547. Number of Provinces
# Difficulty: Medium
# Date: 2021-07-25


from collections import defaultdict

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        c = defaultdict(set)

        n = len(isConnected)
        for i in range(n):
            for j in range(n):
                if i != j and isConnected[i][j]:
                    c[i].add(j)
                    c[j].add(i)

        num_provinces = 0
        seen = set()

        def dfs(i):
            if i in seen:
                return
            seen.add(i)
            neighbors = c[i]
            for n in neighbors:
                dfs(n)


        for i in range(n):
            if i not in seen:
                dfs(i)
                num_provinces += 1

        return num_provinces
