class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        memo = {}

        def dpf(amount):

            if amount == 0:
                return 0
            if amount in memo:
                return memo[amount]

            
            res = float("inf")
            for j in range(len(coins)):
                if amount - coins[j] < 0:
                    continue
                res = min(dpf(amount - coins[j]) + 1, res)
            
            memo[amount] = res
            return res
        
        res = dpf(amount)
        return res if res != float("inf") else -1
