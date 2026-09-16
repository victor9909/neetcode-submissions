class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        memo = {}

        def backtrack(i):
            if i in memo:
                return memo[i]

            if i >= len(s):
                return True
            
            res = False
            for w in wordDict:
                len_w = len(w)
                if i + len_w <= len(s) and s[i: i + len_w] == w:
                    res |= backtrack(i + len(w))
            memo[i] = res
            return res
        
        return backtrack(0)
                