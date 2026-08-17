class Solution:
    def climbStairs(self, n: int) -> int:
        
        cache = {n: 1}

        def dpf(i):

            if i in cache:
                return cache[i]

            if i >= n:
                return 1
            
            cache[i] = dpf(i + 1) + dpf(i + 2)
            return cache[i]
        
        return dpf(1)
