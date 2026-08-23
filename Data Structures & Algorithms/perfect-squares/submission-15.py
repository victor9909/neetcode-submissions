class Solution:
    def numSquares(self, n: int) -> int:
        memo = {}

        def dfs(target):
            if target == 0:
                return 0

            if target in memo:
                return memo[target]

            res = float("inf")

            for i in range(1, int(target ** 0.5) + 1):
                
                square = i * i
                if target - square < 0:
                    break
                res = min(res, dfs(target - square) + 1)

            memo[target] = res
            return res

        #return dfs(n)

        dp = [float("inf")] * (n + 1)
        dp[n] = 0
        for i in range(n - 1, -1, -1):
            for e in range(1, int(n ** 0.5) + 1):
                square = e * e
                if i + square <= n:
                    dp[i] = min(dp[i], dp[i + square] + 1)
        return dp[0]

