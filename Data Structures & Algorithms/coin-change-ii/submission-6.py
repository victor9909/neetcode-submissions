class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        memo = {}
        def dfs(i, target):
            
            if (i, target) in memo:
                return memo[(i, target)]

            if target == 0:
                return 1
            
            if target < 0 or i >= len(coins):
                return 0
            
            
            memo[(i, target)] = dfs(i, target - coins[i]) + dfs(i + 1, target)
            return memo[(i, target)]
        
        return dfs(0, amount)