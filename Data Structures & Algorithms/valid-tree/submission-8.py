class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        adj_list = defaultdict(list)
        for x, y in edges:
            adj_list[x].append(y)
            adj_list[y].append(x)
        
        visit = set()

        def dfs(node, par):

            if node in visit:
                return False
            
            visit.add(node)
            for nei in adj_list[node]:
                if nei == par:
                    continue
                if not dfs(nei, node):
                    return False
                
            return True
        
        
        res = dfs(0, -1)
        print(len(visit))
        return res if len(visit) == n else False



