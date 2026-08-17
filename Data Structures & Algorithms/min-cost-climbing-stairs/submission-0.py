class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        cache = {}

        def backtrack(idx):
            if idx in cache:
                return cache[idx]
            
            if idx >= len(cost):
                return 0
            
            res = cost[idx] + min(backtrack(idx + 1), backtrack(idx + 2))
            cache[idx] = res
            return cache[idx]

        return min(backtrack(0), backtrack(1))


