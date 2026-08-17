class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        memo = {}
        def dpf(amount):
            
            if amount == 0:
                return 0
            
            if amount in memo:
                return memo[amount]

            res = 1e9
            for c in coins:
                if amount - c >= 0:
                    res = min(res, 1 + dpf(amount - c))
            memo[amount] = res
            return res
        
        dp = [float('inf')] * (amount + 1)
        dp[amount] = 0

        for i in range(amount, -1, -1):
            for c in coins:
                if i - c >= 0:
                    dp[i - c] = min(dp[i - c], dp[i] + 1)

        return dp[0] if dp[0] != float("inf") else -1
