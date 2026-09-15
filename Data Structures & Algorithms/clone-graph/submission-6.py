"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        dict_clone = {None:None}
        visit = set()

        def dfs(node):

            if node in dict_clone:
                return dict_clone[node]

            visit.add(node)
            n = Node(node.val)
            dict_clone[node] = n

            for nei in node.neighbors:
                
                dict_clone[node].neighbors.append(dfs(nei))
            
            return n

        dfs(node)
        return dict_clone[node]

