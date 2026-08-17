class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        memo = {len(cost): 0}
        def backtrack(i):
            if i in memo:
                return memo[i]
            if i >= len(cost):
                return 0
            
            res = cost[i] + min(backtrack(i + 1), backtrack(i + 2))
            memo[i] = res
            return res
        
        #return min(backtrack(0), backtrack(1))

        n = len(cost)
        dp = [0] * (n + 3)
        for i in range(n - 1, -1, -1):
            dp[i] = cost[i] + min(dp[i + 1], dp[i + 2])
        
        return min(dp[0], dp[1])



            