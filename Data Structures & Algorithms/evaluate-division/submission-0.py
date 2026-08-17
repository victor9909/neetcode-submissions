class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        adj_list = defaultdict(list)
        for i, item in enumerate(equations):
            adj_list[item[0]].append((item[1], values[i]))
            adj_list[item[1]].append((item[0], 1/values[i]))
        
        cache = {}

        def dfs(src, dst, visit):

            if src not in adj_list or dst not in adj_list:
                return -1
            
            if src == dst:
                return 1
            
            if (src, dst) in cache:
                return cache[(src, dst)]

            visit.add(src)
            for var, val in adj_list[src]:
                if var in visit:
                    continue
                result = dfs(var, dst, visit)
                if result != -1:
                    cache[(src, dst)] = val * result
                    cache[(dst, src)] = 1 / (val * result)  # inverso gratis
                    return cache[(src, dst)]
            
            return -1
        
        res = []
        for src, dst in queries:
            res.append(dfs(src, dst, set()))
        return res
