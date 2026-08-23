class Solution:
    def numDecodings(self, s: str) -> int:
        
        memo = {}

        def dfs(i):
            if i in memo:
                return memo[i]
            if i >= len(s):
                return 1
            
            res = 0
            if s[i] in "123456789":
                res += dfs(i + 1)
            if i + 1 < len(s) and (s[i] in "1" and s[i + 1] in "0123456789") or (i + 1 < len(s) and s[i] == "2" and s[i + 1] in "0123456"):
                res += dfs(i + 2)
            memo[i] = res
            return res
        
        #return dfs(0)

        dp = [0] * (len(s) + 1)
        dp[len(s)] = 1
        for i in range(len(s) - 1, - 1, -1):
            if s[i] in "123456789":
                dp[i] = dp[i + 1]
            if i + 1 < len(s) and (s[i] in "1" and s[i + 1] in "0123456789") or (i + 1 < len(s) and s[i] == "2" and s[i + 1] in "0123456"):
                dp[i] += dp[i + 2]
        
        return dp[0]


