class Solution:
    def climbStairs(self, n: int) -> int:
        
        memo = {}

        def dpf(i: int):
            
            if i in memo:
                return memo[i]

            if i == n:
                return 1

            if i > n:
                return 0

            memo[i] = dpf(i + 1) + dpf(i + 2)
            return memo[i]
        
        #return dpf(0)

        dp = [0] * (n + 1)
        dp[n] = 1
        dp[n-1] = 1
        for i in range(n-2, -1, -1):
            dp[i] = dp[i + 1] + dp[i+2]
        return dp[0]


