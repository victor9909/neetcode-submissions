class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        parent = [i for i in range(n)]
        rank = [1] * n

        def find(n):

            par = parent[n]
            while par != parent[par]:
                par = parent[par]
            return par

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return False
            
            if rank[p1] > rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]
            return True

        components = 0
        for u, v in edges:
            if not union(u, v):
                return False
            components += 1
        return components == n - 1
