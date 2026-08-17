class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        dict_judges = {i:set() for i in range(1, n+1, 1)}
        for x, y in trust:
            dict_judges[x].add(y)

        judge = -1
        for k in dict_judges:
            if len(dict_judges[k]) == 0:
                judge = k

        for k in dict_judges:
            if k != judge and judge not in dict_judges[k]:
                return -1

        return judge
        
     