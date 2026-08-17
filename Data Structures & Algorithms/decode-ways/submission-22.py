class Solution:
    def numDecodings(self, s: str) -> int:
        
        memo = {len(s): 1}

        def backtrack(i):
            if i in memo:
                return memo[i]
            if i >= len(s):
                return 1

            res = 0
            if s[i] in "123456789":
                res += backtrack(i + 1)

            if i + 1 < len(s) and (
                s[i] == "1" and s[i + 1] in "0123456789" or s[i] == "2" and s[i + 1] in "0123456"
            ):
                res += backtrack(i + 2)

            memo[i] = res
            return res

        #return backtrack(0)
        n = len(s)
        dp = [1] * (n + 3)
        for i in range(n - 1, -1, -1):
            dp[i] = 0
            if s[i] in "123456789":
                dp[i] += dp[i + 1]
            if i + 1 < len(s) and (
                s[i] == "1" and s[i + 1] in "0123456789" or s[i] == "2" and s[i + 1] in "0123456"
            ):
                dp[i] += dp[i + 2]
        
        return dp[0]
