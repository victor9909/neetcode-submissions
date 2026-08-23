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
        
        return dfs(0)