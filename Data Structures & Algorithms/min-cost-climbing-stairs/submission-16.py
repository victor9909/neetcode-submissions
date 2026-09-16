class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        memo = {len(cost): 0}

        def backtrack(i):

            if i in memo:
                return memo[i]

            if i >= len(cost):
                return 0
            
            memo[i] = cost[i] + min(backtrack(i + 1), backtrack(i + 2))
            return memo[i]
        
        #return min(backtrack(0), backtrack(1))

        dp = [0] * len(cost)
        dp[0] = cost[0]
        dp[1] = cost[1]

        for i in range(2, len(cost)):
            dp[i] = min(dp[i - 1], dp[i - 2]) + cost[i]
        return min(dp[-1], dp[-2])
        


