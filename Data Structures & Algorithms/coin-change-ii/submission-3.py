class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        memo = {}

        def dfs(idx, curr):
            
            if curr == amount:
                return 1
            
            if curr > amount or idx >= len(coins):
                return 0

            if (idx, curr) in memo:
                return memo[(idx, curr)]
            
            res = 0
            res += dfs(idx + 1, curr)
            res += dfs(idx, curr  + coins[idx])
            
            memo[(idx, curr)] = res
            return memo[(idx, curr)]

        return dfs(0, 0)
