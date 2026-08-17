class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        memo = {}

        def dpf(i):

            if i >= len(s):
                return True
            
            if i in memo:
                return memo[i]

            res = False
            for w in wordDict:
                if s[i:i+len(w)] == w:
                    res |= dpf(i + len(w))
            
            memo[i] = res
            return res
        
        #return dpf(0)


        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                if (i + len(w)) <= len(s) and s[i : i + len(w)] == w:
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break

        return dp[0]

