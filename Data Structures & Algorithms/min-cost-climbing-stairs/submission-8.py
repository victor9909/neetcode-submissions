class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        memo = {}

        def dpf(i: int):

            if i in memo:
                return memo[i]

            if i >= len(cost):
                return 0
            
            memo[i] = min(dpf(i + 1), dpf(i + 2)) + cost[i]
            return memo[i]
        
        #return min(dpf(0), dpf(1))

        dp = [0] * (len(cost) + 1)
        dp[len(cost) - 1] = cost[-1]
        for i in range(len(cost) - 2, -1, -1):
            dp[i] = min(dpf(i + 1), dpf(i+2)) + cost[i]
        
        return min(dp[0], dp[1])
