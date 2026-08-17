class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        adj_list = defaultdict(list)
        for src, dst in prerequisites:
            adj_list[src].append(dst)
        
        def dfs(src, dst, visit):

            
            if src == dst:
                return True
            
            visit.add(src)
            for cr in adj_list[src]:
                if cr in visit:
                    continue
                if dfs(cr, dst, visit):
                    return True
            return False
        
        res = []
        for cr, pre in queries:
            res.append(dfs(cr, pre, set()))
        return res