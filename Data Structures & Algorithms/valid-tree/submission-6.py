class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        # not valid
        #        ------> 4
        # 0 -> 1 -> 2 -> 3
        #        ------> 3

        # valid
        #      3  
        # 0 -> 1 -> 4
        #      2 
        
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        print(adj)
        visit = set()
        def dfs(node, par):
            if node in visit:
                return False
            
            visit.add(node)
            for nei in adj[node]:
                if nei == par:
                    continue
                if not dfs(nei, node):
                    return False
            return True

        return dfs(0, -1) and len(visit) == n