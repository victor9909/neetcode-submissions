class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        if n == 0:
            return True
        
        prevMap = { i: [] for i in range(n) }
        for n1, n2 in edges:
            prevMap[n1].append(n2)
            prevMap[n2].append(n1)
        
        visit = set()
        def dfs(i, prev):
            if i in visit:
                return False
            
            visit.add(i)
            for node in prevMap[i]:
                if node == prev:
                    continue
                if not dfs(node, i):
                    return False
            
            return True
        
        return dfs(0, -1) and len(visit) == n
            
