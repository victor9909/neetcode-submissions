class Solution:
    def tribonacci(self, n: int) -> int:
        
        memo = {}

        def dfs(i):
            if i in memo:
                return memo[i]
            if i == 0:
                return 0
            
            if i <= 2:
                return 1
            memo[i] = dfs(i - 3) + dfs(i - 2) + dfs(i - 1)
            return memo[i]
        
        #return dfs(n)

        if n == 0:
            return 0
        if n <= 2:
            return 1
        dp = [0] * (n + 1)
        dp[-2] = 1
        dp[-3] = 1
        print(dp)
        for i in range(n - 3, -1, -1):
            dp[i] = dp[i + 3] + dp[i + 2] + dp[i + 1]
        print(dp)
        return dp[0]

