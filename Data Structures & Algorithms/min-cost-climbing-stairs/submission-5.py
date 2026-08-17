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
        
        #return min(dp(0), dp(1))

        dp_arr = [0] * (len(cost))
        dp_arr[0] = cost[0]
        dp_arr[1] = cost[1]

        for i in range(2, len(cost)):
            dp_arr[i] = cost[i] + min(dp_arr[i - 1], dp_arr[i - 2])
        
        return min(dp_arr[-1], dp_arr[-2])


