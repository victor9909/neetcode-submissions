class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # (idx, buying)
        memo = {}

        def dfs(idx, buying):

            if (idx, buying) in memo:
                return memo[(idx, buying)]
            if idx >= len(prices):
                return 0

            
            cooldown = dfs(idx + 1, buying)
            if buying:
                buy = dfs(idx + 1, not buying) - prices[idx]
                memo[(idx, buying)] = max(buy, cooldown)
                return memo[(idx, buying)]
            else:
                sell = dfs(idx + 2, not buying) + prices[idx]
                memo[(idx, buying)] = max(sell, cooldown)
                return memo[(idx, buying)]
        
        return dfs(0, True)