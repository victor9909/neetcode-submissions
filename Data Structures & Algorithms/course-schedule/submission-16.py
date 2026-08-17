class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adj_list = {}
        for i in range(numCourses):
            adj_list[i] = []
        
        for pre, crs in prerequisites:
            adj_list[pre].append(crs)

        def dfs(crs, visit):

            if crs in visit:
                return False
            
            visit.add(crs)
            for course in adj_list[crs]:
                if not dfs(course, visit):
                    
                    return False
            visit.remove(crs)

            return True

        for i in range(numCourses):
            new_vis = set()
            if not dfs(i, new_vis):
                return False
        
        return True
