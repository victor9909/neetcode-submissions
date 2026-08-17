class Solution:
    def numDecodings(self, s: str) -> int:
        
        memo = {}

        def dpf(i):

            if i in memo:
                return memo[i]

            if i >= len(s):
                return 1
            
            if s[i] == "0":
                return 0
            
            res = dpf(i + 1)

            if i + 1 < len(s) and (
                s[i] == "1" or s[i] == "2" and
                s[i + 1] in "0123456"
            ):
                res += dpf(i + 2)
            
            memo[i] = res
            return res
        
        #return dpf(0)

        dp = {len(s): 1}
        for i in range(len(s) - 1, -1, -1):
            if s[i] == "0":
                dp[i] = 0
            else:
                dp[i] = dp[i + 1]

            if i + 1 < len(s) and (s[i] == "1" or
               s[i] == "2" and s[i + 1] in "0123456"
            ):
                dp[i] += dp[i + 2]
        return dp[0]
