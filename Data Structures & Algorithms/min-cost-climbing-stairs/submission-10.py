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
        
        return min(backtrack(0), backtrack(1))
            