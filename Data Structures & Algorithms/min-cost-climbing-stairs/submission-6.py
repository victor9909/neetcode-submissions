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
        
        return min(dpf(0), dpf(1))