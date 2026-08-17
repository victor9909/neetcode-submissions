class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adj_list = defaultdict(list)
        for i, j in prerequisites:
            adj_list[i].append(j)

        
        def dfs(crs, visit):

            if crs in visit:
                return False
            
            visit.add(crs)
            for pre in adj_list[crs]:
                if not dfs(pre, visit):
                    return False
            visit.remove(crs)
            return True

        for crs in range(numCourses):
            if not dfs(crs, set()):
                return False
        return True
