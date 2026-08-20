class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adj_list = {crs: [] for crs in range(numCourses)}
        for u, v in prerequisites:
            adj_list[u].append(v)
        
        visit = set()
        def dfs(cr):
            if cr in visit:
                return False
            
            if adj_list[cr] == []:
                return True
            
            visit.add(cr)
            for c in adj_list[cr]:
                if not dfs(c):
                    return False
            visit.remove(cr)
            adj_list[cr] = []
            
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True