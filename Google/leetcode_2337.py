# Problem: 841. Keys a
# Difficulty: Medium
# Date: 2025-05-12

class Solution:
    def canChange(self, start: str, target: str) -> bool:
        if len(start) != len(target):
            return False
            
        len_i = len(start)
        len_t = len(target)
        pi = pt = 0
        
        while pi < len_i or pt < len_t:
            
            while pi < len_i and start[pi] == '_':
                pi += 1
                
            while pt < len_t and target[pt] == '_':
                pt += 1
                
            if pi == len_i and pt == len_t:
                break
                
            if (pi == len_i and pt < len_t) or (pt == len_t and pi < len_i) or start[pi] != target[pt]:
                return False
                
            if (start[pi] == 'L' and pi < pt) or (start[pi] == 'R' and pi > pt):
                return False
                
            pi += 1
            pt += 1
        
        return True