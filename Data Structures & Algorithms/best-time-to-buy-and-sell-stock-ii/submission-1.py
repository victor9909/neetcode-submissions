class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}

        def dfs(i, bought):

            if (i, bought) in memo:
                return memo[(i, bought)]

            if i >= len(prices):
                return 0
            
            res = dfs(i + 1, bought)
            if bought:
                res = max(res, prices[i] + dfs(i + 1, False))
            else:
                res = max(res, -prices[i] + dfs(i + 1, True))
            memo[(i, bought)] = res
            return res
        
        return dfs(0, False)