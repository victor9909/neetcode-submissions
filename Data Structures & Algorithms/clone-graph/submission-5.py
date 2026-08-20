"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        dict_clone = defaultdict(lambda: Node())
        if not node:
            return None
            
        def dfs(child):

            if child.val in dict_clone:
                return dict_clone[child.val]
            
            dict_clone[child.val].val = child.val
            for nei in child.neighbors:
                dict_clone[child.val].neighbors.append(dfs(nei))
            
            return dict_clone[child.val]
        
        dfs(node)
        return dict_clone[node.val]
