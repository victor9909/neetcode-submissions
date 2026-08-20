class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        rank = [1] * (n)
        par = [i for i in range(n)]

        def find(node):
            p = node
            while p != par[p]:
                p = par[p]
            return p
        
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
        
        components = n
        for u, v in edges:
            if union(u, v):
                components -= 1
        
        return components
