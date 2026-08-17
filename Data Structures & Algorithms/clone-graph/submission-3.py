"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        dict_clone = {}
        visit = set()
        if not node:
            return None
        
        def dfs(curr):
            if curr in visit:
                return dict_clone[curr]
            
            visit.add(curr)
            clone = Node(curr.val)
            dict_clone[curr] = clone
            for nei in curr.neighbors:
                clone.neighbors.append(dfs(nei))
            return clone
        dfs(node)
        return dict_clone[node]