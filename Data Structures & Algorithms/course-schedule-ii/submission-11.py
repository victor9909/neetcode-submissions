class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        adj_list = defaultdict(list)
        for pre, crs in prerequisites:
            adj_list[pre].append(crs)
        
        res = []
        cycle = set()
        visit = set()

        def dfs(crs):

            if crs in cycle:
                return False
            
            if crs in visit:
                return True

            cycle.add(crs)
            visit.add(crs)
            

            for cr in adj_list[crs]:
                if not dfs(cr):
                    return False
            cycle.remove(crs)
            res.append(crs)
            
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        return res
