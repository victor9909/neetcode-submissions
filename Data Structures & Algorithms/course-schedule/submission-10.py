class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adj = defaultdict(list)
        for x, y in prerequisites:
            adj[x].append(y)
        
        path = set()

        def dfs(c):

            if c in path:
                return False
            
            path.add(c)
            for pre in adj[c]:
                if not dfs(pre):
                    return False

            path.remove(c)

            return True
        
        for i in range(1, numCourses):
            if not dfs(i):
                return False
        
        return True

