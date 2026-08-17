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
        
        return dfs(0)
