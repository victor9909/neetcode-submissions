class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        adj_list = {i: [] for i in range(numCourses)}
        indegree = [0] * numCourses

        for crs, pre in prerequisites:
            adj_list[pre].append(crs)
            indegree[crs] += 1

        q = deque()

        for crs in range(numCourses):
            if indegree[crs] == 0:
                q.append(crs)

        res = []

        while q:
            crs = q.popleft()
            res.append(crs)
            for nei in adj_list[crs]:
                indegree[nei] -= 1

                if indegree[nei] == 0:
                    q.append(nei)

        if len(res) != numCourses:
            return []

        return res