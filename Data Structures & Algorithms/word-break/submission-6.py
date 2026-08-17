class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        # s = "neetcode", wordDict = ["neet","code"]
        # "neet" idx = 0 -> 0 - 3 ? yes -> idx = 4
        # "neet" idx = 4 -> 4 - 8 ? No
        # "code" idx = 4 -> 4 - 8 ? Yes 
        # idx = 8 > len -> True

        memo = {len(s): True}
        def dp(idx):

            if idx in memo:
                return memo[idx]
            
            res = False
            for w in wordDict:
                if s[idx: idx + len(w)] == w:
                    res |= dp(idx + len(w))
                
            memo[idx] = res
            return res
        
        return dp(0)
        
