class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        memo = {len(s): True}

        def dfs(i):
            if i in memo:
                return memo[i]

            if i >= len(s):
                return True
            
            res = False
            for w in wordDict:
                if i + len(w) <= len(s) and s[i: i + len(w)] == w:
                    res |= dfs(i + len(w))
            memo[i] = res
            return res
        
        #return dfs(0)

        dp = [False] * (len(s) + 1)
        
        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                if i + len(w) <= len(s) and s[i: i + len(w)] == w:
                    dp[i] |= dp[i + len(w)] if i + len(w) < len(s) else True
        
        return dp[0]
