class Solution:
    def climbStairs(self, n: int) -> int:
        
        memo = {}

        def dp(curr):
            
            if curr in memo:
                return memo[curr]

            if curr < 0:
                return 0
            if curr == 0:
                return 1
            
            memo[curr] = dp(curr - 1) + dp(curr - 2)
            return memo[curr]

        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        
        if n <= 2:
            return n

        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        
        return dp[n]
