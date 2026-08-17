class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        dict_cours = dict()
        for c in range(numCourses):
            dict_cours[c] = []

        for p, q in prerequisites:
            dict_cours[p].append(q)
        
        visit = set()
        
        def dfs(c):

            if c in visit:
                return False
            if dict_cours[c] == []:
                return True

            visit.add(c)
            for pre in dict_cours[c]:
                if not dfs(pre):
                    return False
            visit.remove(c)
            dict_cours[c] = []
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        
        return True

