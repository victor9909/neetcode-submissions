class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        dict_courses = defaultdict(list)
        for p, q in prerequisites:
            dict_courses[p].append(q)
        
        visit, cycle = set(), set()
        res = []

        def dfs(c):
            if c in cycle:
                return False
            if c in visit:
                return True
            
            cycle.add(c)
            for pre in dict_courses[c]:
                if not dfs(pre):
                    return False
            
            cycle.remove(c)
            visit.add(c)
            res.append(c)
            
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return []
        
        return res
