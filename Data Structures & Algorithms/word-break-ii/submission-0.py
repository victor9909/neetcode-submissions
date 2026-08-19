class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        res = []
        word_set = set(wordDict)

        def backtrack(i, curr):

            if i >= len(s):
                res.append(" ".join(curr[::]))
                return
            
            for j in range(i, len(s)):
                if s[i:j + 1] not in word_set:
                    continue
                curr.append(s[i: j + 1])
                backtrack(j + 1, curr)
                curr.pop()
        
        backtrack(0, [])
        return res