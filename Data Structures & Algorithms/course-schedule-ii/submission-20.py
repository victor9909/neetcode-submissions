class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        

        adj_list = {i:[] for i in range(numCourses)}
        for u, v in prerequisites:
            adj_list[u].append(v)
        
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
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        
        return res


