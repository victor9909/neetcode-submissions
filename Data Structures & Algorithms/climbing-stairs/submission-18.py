class Solution:
    def climbStairs(self, n: int) -> int:
        
        memo = {}

        def dfs(i):
            if i in memo:
                return memo[i]
            if i >= n:
                return 1
            
            memo[i] = dfs(i + 1) + dfs(i + 2)
            return memo[i]
        
        #return dfs(1)
        
        dp = [0] * (n + 2)
        dp[n] = 1
        dp[n + 1] = 1
        for i in range(n - 1, -1, -1):
            dp[i] = dp[i + 1] + dp[i + 2]
        
        return dp[1]



