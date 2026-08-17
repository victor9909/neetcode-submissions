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
                w_len = len(w)
                if s[i:i+len(w)] == w:
                    res |= dpf(i+len(w))
            memo[i] = res
            return res
        
        return dpf(0)
