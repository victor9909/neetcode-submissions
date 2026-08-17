class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        max_l = float("-inf")
        res_l, res_r = 0, 0
        for i in range(len(s)):

            l, r = i, i
            while l >= 0 and r < len(s) and s[r] == s[l]:
                if max_l < r - l + 1:
                    max_l = r - l + 1
                    res_l, res_r = l, r
                l -= 1
                r += 1
            
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[r] == s[l]:
                if max_l < r - l + 1:
                    max_l = r - l + 1
                    res_l, res_r = l, r
                l -= 1
                r += 1
        
        return s[res_l : res_r + 1]

