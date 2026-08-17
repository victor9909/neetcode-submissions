class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        cache = {len(cost): 0}

        def dp(i):

            if i in cache:
                return cache[i]

            if i >= len(cost):
                return 0
            
            cache[i] = cost[i] + min(dp(i + 1), dp(i + 2))
            return cache[i]
        
        return min(dp(0), dp(1))
