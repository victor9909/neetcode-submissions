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

        #return dfs(0, 0)

        def dp():

            dp = defaultdict(int)
            n = len(coins)
            for i in range(n + 1):
                dp[(i, amount)] = 1
            
            for idx in range(len(coins) - 1, -1, -1):
                for curr in range(amount, -1, -1):
                    dp[(idx, curr)] = dp[(idx + 1, curr)]

                    if curr + coins[idx] <= amount:
                        dp[(idx, curr)] += dp[(idx, curr + coins[idx])]

            return dp[(0, 0)]

            
            
        return dp()




