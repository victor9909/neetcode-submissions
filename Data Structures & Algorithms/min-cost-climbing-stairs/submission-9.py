class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        cache = {len(cost): 0}

        def dpf(i):
            
            if i in cache:
                return cache[i]

            if i >= len(cost):
                return 0
            
            cache[i] = min(dpf(i + 1), dpf(i + 2)) + cost[i]
            return cache[i]
        
        return min(dpf(0), dpf(1))