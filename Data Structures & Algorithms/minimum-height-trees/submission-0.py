class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        
        
        adj_list = {i: [] for i in range(n)}
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        cycle = set()

        def dfs(node):
            
            if node in cycle:
                return 0
            
            res = float("-inf")
            cycle.add(node)
            for nei in adj_list[node]:
                res = max(res, dfs(nei) + 1)
            cycle.remove(node)

            return res
        
        min_h = 0
        res = float("inf")
        dict_min_h = defaultdict(list)
        for n in range(n):
            min_h = dfs(n)
            res = min(res, min_h)
            dict_min_h[min_h].append(n)

        return dict_min_h[res]

        
            
