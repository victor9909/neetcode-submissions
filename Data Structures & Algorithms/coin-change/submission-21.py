class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        memo = {}

        def backtrack(amount):

            if amount in memo:
                return memo[amount]

            if amount == 0:
                return 0
            
            res = float("inf")
            for c in coins:
                if amount - c < 0:
                    continue
                res = min(res, backtrack(amount - c) + 1)
            
            memo[amount] = res
            return res
        
        minCoins = backtrack(amount)
        return minCoins if minCoins != float("inf") else -1

            
            
