class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adj_list = {i:[] for i in range(numCourses)}
        for u, v in prerequisites:
            adj_list[u].append(v)
        
        visit = set()

        def dfs(crs):
            
            if crs in visit:
                return False
            
            visit.add(crs)
            for pre in adj_list[crs]:
                if not dfs(pre):
                    return False
            adj_list[crs] = []
            visit.remove(crs)

            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
        