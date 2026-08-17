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
        
        #return dfs(0, True)

        def dp():
            dp = defaultdict(int)

            for i in range(len(prices) + 1):
                dp[(i, True)] = 0
                dp[(i, False)] = 0

            for i in range(len(prices) - 1, -1, -1):
                for buying in [True, False]:
                    if buying:
                        buy = dp[(i + 1, False)] - prices[i]
                        cooldown = dp[(i+1, True)] 
                        dp[(i, True)] = max(buy, cooldown)
                    else:
                        sell = dp[(i + 2, True)] + prices[i]
                        cooldown = dp[(i+1, False)]
                        dp[(i, False)] = max(sell, cooldown)
                
            return dp[(0, True)]
            
        return dp()







