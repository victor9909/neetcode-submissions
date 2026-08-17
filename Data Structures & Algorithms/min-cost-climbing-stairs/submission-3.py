class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        memo = {}
        def dp(curr, idx):

            if (idx, curr) in memo:
                return memo[(idx, curr)]

            if idx >= len(cost):
                return curr
            
            left = dp(curr + cost[idx], idx + 1)
            right = dp(curr + cost[idx], idx + 2)

            res = min(left, right)
            memo[(idx, curr)] = res
            return memo[(idx, curr)]
        
        #return min(dp(0, 0), dp(0, 1))

        dp = [0] * (len(cost) + 1)
        dp[0] = cost[0]
        dp[1] = cost[1]

        for i in range(2, len(cost) + 1):
            curr_cost = cost[i] if i < len(cost) else 0
            dp[i] = min(dp[i - 1] + curr_cost, dp[i - 2] + curr_cost)
        
        return min(dp[-2], dp[-1])
        



