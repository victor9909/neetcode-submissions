class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        par = [i for i in range(len(edges) + 1)]
        rank = [1] * (len(edges) + 1)

        def find(n1):
            res = n1

            while res != par[n1]:
                par[n1] = par[par[n1]]
                res = par[n1]
            return res
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return False
            
            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]

            return True
        
        for u, j in edges:
            if not union(u, j):
                return [u, j]