class Solution:
    def isHappy(self, n: int) -> bool:
        
        visit = set()
        str_n = str(n)
        while str_n != "1":
            curr = 0
            for c in str_n:
                curr += int(c) * int(c)
            if curr in visit:
                return False
            str_n = str(curr)
            visit.add(curr)

        return True