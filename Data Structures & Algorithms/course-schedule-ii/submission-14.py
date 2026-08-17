class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        adj_list = defaultdict(list)
        for i, j in prerequisites:
            adj_list[i].append(j)
        
        cycle = set()
        visit = set()
        res = []

        def dfs(crs):
        
            if crs in cycle:
                return False
            
            if crs in visit:
                return True
            
            cycle.add(crs)
            visit.add(crs)
            
            for pre in adj_list[crs]:
                if not dfs(pre):
                    return False
            cycle.remove(crs)
            res.append(crs)
            
            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return []
        
        return res
