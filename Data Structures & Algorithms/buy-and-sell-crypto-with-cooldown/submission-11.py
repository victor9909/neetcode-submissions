class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        memo = {}

        def dfs(buy, i):

            if (i, buy) in memo:
                return memo[(i, buy)]

            if i >= len(prices):
                return 0
            
            res = dfs(buy, i + 1)
            if buy:
                res = max(res, -prices[i] + dfs(False, i + 1))
            else:
                res = max(res, prices[i] + dfs(True, i + 2))
            
            memo[(i, buy)] = res
            return res
        
        return dfs(True, 0)