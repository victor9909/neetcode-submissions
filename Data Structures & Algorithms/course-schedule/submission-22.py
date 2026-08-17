class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adj_list = { i:[] for i in range(numCourses) }
        for crs, pre in prerequisites:
            adj_list[crs].append(pre)
        
        visit = set()

        def dfs(crs):

            if adj_list[crs] == []:
                return True
            
            if crs in visit:
                return False
            
            visit.add(crs)
            for cr in adj_list[crs]:
                if not dfs(cr):
                    return False
            visit.remove(crs)
            return True

        
        for n in range(numCourses):
            if not dfs(n):
                return False
        
        return True
