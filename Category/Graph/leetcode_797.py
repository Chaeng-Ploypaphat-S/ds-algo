from typing import List

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        target = len(graph) - 1
        res = []
        
        paths = [[0]]
        while paths:
            path = paths.pop()
    
            for node in graph[path[-1]]:
                new_path = path.copy() + [node]
                if node == target:
                    res.append(new_path)
                else:
                    paths.append(new_path)

        return res