class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        adj_list = {crs:[] for crs in range(numCourses)}
        for crs, pre in prerequisites:
            adj_list[crs].append(pre)
        
        cycle = set()
        visit = set()
        res = []

        def dfs(course):
            
            
            if course in cycle:
                return False
            if course in visit:
                return True
            
            visit.add(course)
            cycle.add(course)
            for crs in adj_list[course]:
                if not dfs(crs):
                    return False
            cycle.remove(course)
            res.append(course)

            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return []
        return res