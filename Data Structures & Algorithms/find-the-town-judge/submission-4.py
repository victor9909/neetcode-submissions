class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        adj_list = {i:[0, 0] for i in range(1, n + 1)}
        for u, v in trust:
            adj_list[u][1] += 1
            adj_list[v][0] += 1

        for k in adj_list:
            if adj_list[k][0] == n - 1 and adj_list[k][1] == 0:
                return k
        return -1
