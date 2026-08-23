class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        memo = {}
        def dfs(i):
            if i in memo:
                return memo[i]
            if i >= len(s):
                return True
            
            res = False
            for w in wordDict:
                len_w = len(w)
                if s[i: i + len_w] == w:
                    res |= dfs(i + len_w)
            memo[i] = res
            return res
        
        #return dfs(0)

        dp = [False] * (len(s) + 1)
        dp[len(s)] = True
        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                len_w = len(w)
                if s[i: i + len_w] == w:
                    dp[i] |= dp[i + len(w)]
        
        return dp[0]


