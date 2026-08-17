class Solution:
    def climbStairs(self, n: int) -> int:
        
        cache = {}

        def backtrack(step):
            
            if step in cache:
                return cache[step]
                
            if step == n: 
                return 1
            if step > n:
                return 0
            
            res = backtrack(step + 1) + backtrack(step + 2)
            cache[step] = res
            return res
        
        return backtrack(0)
