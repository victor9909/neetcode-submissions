class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        memo = {}

        def dp(amount):
            if amount in memo:
                return memo[amount]
                
            if amount == 0:
                return 0
            
            res = 1e9
            for c in coins:
                if amount - c >= 0:
                    res = min(res, 1 + dp(amount - c))
            memo[amount] = res
            return memo[amount]
        
        minCoins = dp(amount)
        return minCoins if minCoins != 1e9 else -1
