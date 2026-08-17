class Solution:
    def numDecodings(self, s: str) -> int:
        
        cache = {len(s): 1}

        def dpf(i: int):

            if i in cache:
                return cache[i]

            if i >= len(s):
                return 1
            
            res = 0
            if s[i] in "123456789":
                res += dpf(i + 1)
            
            if i + 1 < len(s) and 10 <= int(s[i: i + 2]) <= 26:
                res += dpf(i + 2)

            cache[i] = res

            return res

        #return dpf(0)

        dp = [0] * (len(s) + 1)
        dp[len(s)] = 1

        for i in range(len(s) - 1, -1, -1):
            if s[i] in "123456789":
                dp[i] += dp[i + 1]
            if i + 1 < len(s) and 10 <= int(s[i: i + 2]) <= 26:
                dp[i] += dp[i + 2]
        
        return dp[0]


