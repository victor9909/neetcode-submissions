class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        memo = {}
        def dp(amount):
            
            if amount == 0:
                return 0
            
            if amount in memo:
                return memo[amount]

            res = 1e9
            for c in coins:
                if amount - c >= 0:
                    res = min(res, 1 + dp(amount - c))
            memo[amount] = res
            return res
        
        min_coins = dp(amount)
        return -1 if min_coins == 1e9 else min_coins
