class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        par = list(range(len(edges) + 1))
        rank = [0] * (len(edges) + 1)

        adj_list = {i:[] for i in range(len(edges)+1)}
        for x, y in edges:
            adj_list[x].append(y)
            adj_list[y].append(x)
        
        def find(n1):
            curr = n1
            while curr != par[curr]:
                par[curr] = par[par[curr]]
                curr = par[curr]
            
            return curr
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return False
            
            if rank[p1] > rank[p2]:
                rank[p1] += rank[p2]
                par[p2] = par[p1]
            else:
                rank[p2] += rank[p1]
                par[p1] = par[p2]
            
            return True
        
        for x, y in edges:
            if not union(x, y):
                return [x, y]





        