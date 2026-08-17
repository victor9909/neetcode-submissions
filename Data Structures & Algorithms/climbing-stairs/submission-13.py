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
        
        #return dpf(1)

        dp = [0] * (n + 2)
        dp[-1] = 1
        dp[-2] = 1

        for i in range(n - 1, -1, -1):
            dp[i] = dp[i + 1] + dp[i + 2]
        
        return dp[1]

