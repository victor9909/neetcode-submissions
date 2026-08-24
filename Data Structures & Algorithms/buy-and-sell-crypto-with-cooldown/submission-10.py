class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        memo = {}

        def dfs(buy, i):
            if (i, buy) in memo:
                return memo[(i, buy)]

            if i >= len(prices):
                return 0
            
            cooldown = dfs(buy, i + 1)
            if buy:
                res = dfs(not buy, i + 1) - prices[i]
                memo[(i, buy)] = max(cooldown, res)
                return memo[(i, buy)]
            else:
                res = dfs(not buy, i + 2) + prices[i]
                memo[(i, buy)] = max(cooldown, res)
                return memo[(i, buy)]
        
        return dfs(True, 0)
