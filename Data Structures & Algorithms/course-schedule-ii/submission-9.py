class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        adj = defaultdict(list)
        for x, y in prerequisites:
            adj[x].append(y)
        
        visit = set()
        cycle = set()
        res = []

        def dfs(crs):

            if crs in cycle:
                return False
            
            if crs in visit:
                return True

            cycle.add(crs)
            
            for pre in adj[crs]:
                if not dfs(pre):
                    return False
            
            visit.add(crs)
            res.append(crs)
            cycle.remove(crs)
            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return []
        
        return res

        
        