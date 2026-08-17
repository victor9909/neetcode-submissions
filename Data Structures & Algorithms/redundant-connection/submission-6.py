class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        rank = [1] * (len(edges) + 1)
        par = [i for i in range(len(edges) + 1)]

        def find(u):
            u = par[u]
            while u != par[u]:
                u = par[u]
            return u
        
        def union(u, v):
            p1, p2 = find(u), find(v)
            
            if p1 == p2:
                return False
            
            if rank[p1] > rank[p2]:
                rank[p1] += rank[p2]
                par[p2] = p1
            else:
                rank[p2] += rank[p1]
                par[p1] = p2
            
            return True
        
        for u, v in edges:
            
            if not union(u, v):
                return [u, v]
        
