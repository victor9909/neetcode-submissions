class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        dict_courses = {}
        for c in range(numCourses):
            dict_courses[c] = []

        for c, p in prerequisites:
            dict_courses[c].append(p)
        

        def dfs(c, visit):

            if c in visit:
                return False
            
            if dict_courses[c] == []:
                return True

            visit.add(c)
            for pre in dict_courses[c]:
                if not dfs(pre, visit):
                    return False
            visit.remove(c)
            
            return True
    
        for c in range(numCourses):
            if not dfs(c, set()):
                return False
        return True