# Problem: 865. Smallest Subtree with all the Deepest Nodes
# Difficulty: Medium
# Date: 2025-03-16

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        deepest = 0
        deepest_nodes = []
        q = [(root, 0)]
        while q:
            node, depth = q.pop()
            if depth == deepest:
                deepest_nodes.append(node)
            if depth > deepest:
                deepest_nodes = [node]
                deepest = depth
            if node.left:
                q.append((node.left, depth+1))
            if node.right:
                q.append((node.right, depth+1))
        
        def lowest_common_ancestor(node, n1, n2):
            if not node:
                return None
            
            if node == n1 or node == n2:
                return node

            l = lowest_common_ancestor(node.left, n1, n2)
            r = lowest_common_ancestor(node.right, n1, n2)
            if l and r:
                return node
            
            return l or r

        while len(deepest_nodes) >= 2:
            n1 = deepest_nodes.pop()
            n2 = deepest_nodes.pop()

            lca = lowest_common_ancestor(root, n1, n2)
            deepest_nodes.append(lca)

        return deepest_nodes[0]