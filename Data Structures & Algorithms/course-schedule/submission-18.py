class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adj_list = defaultdict(list)
        for crs, pre in prerequisites:
            adj_list[crs].append(pre)
        
        def dfs(crs, cycle):

            if crs in cycle:
                return False
            
            cycle.add(crs)
            for nei in adj_list[crs]:
                if not dfs(nei, cycle):
                    return False
            
            cycle.remove(crs)

            return True
        
        for crs in range(numCourses):
            if not dfs(crs, set()):
                return False
        return True
        
