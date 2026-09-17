class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        memo = {}

        def dfs(i, trg):

            if (i, trg) in memo:
                return memo[(i, trg)]

            if trg == 0:
                return 1
            
            if trg < 0:
                return 0
            
            res = dfs(i, trg - coins[i])
            for j in range(i + 1, len(coins)):
                res += dfs(j, trg - coins[j])
            
            memo[(i, trg)] = res
            return res
        
        return dfs(0, amount)
