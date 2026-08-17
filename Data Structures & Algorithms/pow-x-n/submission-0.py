class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        curr = x if n >= 0 else 1/x
        
        res = 1
        for _ in range(abs(n)):
            res *= curr
        return res
        