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
        first, second = cost[0], cost[1]

        for i in range(2, len(cost)):
            tmp1, tmp2 = first, second
            second = min(first, second) + cost[i]
            first = tmp2

        return min(first, second)
        


