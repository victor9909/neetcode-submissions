class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        char_s = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in char_s:
                char_s.remove(s[l])
                l += 1
            char_s.add(s[r])
            res = max(res, r - l + 1)
        return res