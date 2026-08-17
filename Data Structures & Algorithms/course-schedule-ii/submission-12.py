class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        

        adj_list = defaultdict(list)
        for crs, pre in prerequisites:
            adj_list[crs].append(pre)
        
        visit = set()
        cycle = set()
        res = []

        def dfs(crs):

            if crs in cycle:
                return False
            
            if crs in visit:
                return True
            
            visit.add(crs)
            cycle.add(crs)

            for nei in adj_list[crs]:
                if not dfs(nei):
                    return False
            cycle.remove(crs)
            res.append(crs)
            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return []
        return res



