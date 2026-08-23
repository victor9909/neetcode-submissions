class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        memo = {}
        def dfs(target):
            if target in memo:
                return memo[target]

            if target == 0:
                return 0
            
            res = float("inf")
            for c in coins:
                if target - c < 0:
                    continue
                
                res = min(res, 1 + dfs(target - c))
            memo[target] = res
            return res
        
        min_coins = dfs(amount)
        #return min_coins if min_coins != float("inf") else -1

        dp = [float("inf")] * (amount + 1)
        dp[amount] = 0
        for i in range(amount, -1, -1):
            for c in coins:
                if i + c > amount:
                    continue
                dp[i] = min(dp[i], 1 + dp[i + c])
        
        return dp[0] if dp[0] != float("inf") else -1



