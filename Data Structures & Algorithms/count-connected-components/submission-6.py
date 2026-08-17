class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        rank = [1] * n
        par = [i for i in range(n)]

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
        
        n_unions = 0
        for u, v in edges:
            if union(u, v):
                n_unions += 1
        
        return n - n_unions
