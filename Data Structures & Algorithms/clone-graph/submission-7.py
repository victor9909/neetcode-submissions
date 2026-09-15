"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        if not node:
            return None

        visit = set()
        dict_clone = {None:None}

        def dfs(node):
            

            if node in visit:
                return dict_clone[node]
            
            dict_clone[node] = Node(node.val)
            visit.add(node)
            for nei in node.neighbors:
                dict_clone[node].neighbors.append(dfs(nei))
            
            return dict_clone[node]
        
        return dfs(node)

