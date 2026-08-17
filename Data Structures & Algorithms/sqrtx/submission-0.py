class Solution:
    def mySqrt(self, x: int) -> int:
        
        l, r = 1, x
        res = 0

        while l <= r:
            m = (l + r) // 2
            curr_n = m * m

            if curr_n <= x:
                res = m
                l = m + 1 
            else:
                r = m - 1

        return res
            
