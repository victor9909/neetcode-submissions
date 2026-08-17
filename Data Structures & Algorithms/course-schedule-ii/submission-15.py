class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        adj_list = {i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            adj_list[crs].append(pre)
        
        cycle = set()
        visit = set()
        res = []

        def dfs(crs):
            
            if crs in cycle:
                return False

            if crs in visit:
                return True
            
            visit.add(crs)
            cycle.add(crs)
            for cr in adj_list[crs]:
                if not dfs(cr):
                    return False
            cycle.remove(crs)
            res.append(crs)
            return True

        for n in range(numCourses):
            if not dfs(n):
                return []
        return res
            
            
