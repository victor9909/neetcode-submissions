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
        
        return min(dp(0, 0), dp(0, 1))