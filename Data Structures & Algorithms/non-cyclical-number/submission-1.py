class Solution:
    def isHappy(self, n: int) -> bool:
        
        visit = set()
        while n != 1:
            n_s = str(n)
            res = sum([pow(int(c), 2) for c in n_s])
            if res in visit:
                return False
            n = res
            visit.add(res)
        
        return True