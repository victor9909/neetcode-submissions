class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        memo = {}

        def dfs(i, buy):
            
            if (i, buy) in memo:
                return memo[(i, buy)]

            if i >= len(prices):
                return 0
            
            res = dfs(i + 1, buy)
            if buy:
                res = max(res, -prices[i] + dfs(i + 1, False))
            else:
                res = max(res, prices[i] + dfs(i + 1, True))
            
            memo[(i, buy)] = res
            
            return res
        
        return dfs(0, True)