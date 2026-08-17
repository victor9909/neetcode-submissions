class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        memo = {len(s): True}

        def dpf(i: int):

            if i in memo:
                return memo[i]

            if i >= len(s):
                return True
            
            res = False
            for w in wordDict:
                if i + len(w) > len(s):
                    continue
                if s[i: i + len(w)] == w and dpf(i + len(w)):
                    res |= True
                    
            memo[i] = res
            return res
        
        return dpf(0)
