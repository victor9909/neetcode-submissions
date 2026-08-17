"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        visit = set()
        clone_dict = {}
        if not node:
            return None
        
        def dfs(node):

            if node in visit:
                return clone_dict[node]
            
            visit.add(node)
            clone = Node(node.val)
            clone_dict[node] = clone
            for nei in node.neighbors:
                clone.neighbors.append(dfs(nei))
            
            return clone
        dfs(node)
        return clone_dict[node]