class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        visit = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in visit:
                visit.remove(s[l])
                l += 1
            res = max(r - l + 1, res)
            visit.add(s[r])            
        
        return res