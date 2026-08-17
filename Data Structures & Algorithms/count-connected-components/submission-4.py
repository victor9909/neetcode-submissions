class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        visit = set()

        adj_list = {i:[] for i in range(n)}
        for x, y in edges:
            adj_list[x].append(y)
            adj_list[y].append(x)

        def dfs(node, par):

            if node in visit:
                return
            
            visit.add(node)
            for nei in adj_list[node]:
                if nei == node:
                    continue
                dfs(nei, node)
        
        res = 0
        for i in range(n):
            if i not in visit:
                res += 1
                dfs(i, -1)
        return res
