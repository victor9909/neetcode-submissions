class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        rank = [1] * n
        par = [i for i in range(n)]

        def find(n):
            while n != par[n]:
                n = par[n]
            return n
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

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
            else:
                return False
            
        return n_unions == n - 1
