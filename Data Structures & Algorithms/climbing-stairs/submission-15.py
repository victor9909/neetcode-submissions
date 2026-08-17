class Solution:
    def climbStairs(self, n: int) -> int:
        
        #     0
        #   1   2
        # 2   3
        # v.  x. v
        cache = {n: 1}
        def backtrack(stair):
            
            if stair in cache:
                return cache[stair]
            
            if stair == n:
                return 1
            if stair > n:
                return 0
            
            cache[stair] = backtrack(stair + 1) + backtrack(stair + 2)
            return cache[stair]
        
        #return backtrack(0)

        dp = [0] * (n + 3)
        dp[n] = 1

        for i in range(n - 1, -1, -1):
            dp[i] = dp[i + 1] + dp[i + 2]
        return dp[0]


