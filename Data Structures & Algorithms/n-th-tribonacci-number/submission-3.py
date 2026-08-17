class Solution:
    def tribonacci(self, n: int) -> int:
        
        memo = {}
        
        def dpf(i: int):

            if i <= 0:
                return 0
            if i <= 1:
                return 1
            
            memo[i] = dpf(i - 3) + dpf(i - 2) + dpf(i - 1)
            return memo[i]
        
        #return dpf(n)
        if n <= 2:
            return 0 if n == 0 else 1
        dp = [0] * (n+1)
        dp[1] = 1
        dp[2] = 1

        for i in range(3, n + 1):
            dp[i] = dp[i - 3] + dp[i - 2] + dp[i - 1]
        return dp[n]
