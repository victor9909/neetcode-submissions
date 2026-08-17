class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        trusted = defaultdict(list)
        not_trusted = defaultdict(list)
        for i, j in trust:
            trusted[j].append(i)
            not_trusted[i].append(j)
        
        for i in range(1, n + 1):
            if len(trusted[i]) == n - 1 and len(not_trusted[i]) == 0:
                return i
        return -1

