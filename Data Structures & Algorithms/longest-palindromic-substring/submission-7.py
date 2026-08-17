class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        res = 0
        res_l, res_r = 0, 0
        for i in range(len(s)):

            l, r = i, i
            curr = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > res:
                    res = r - l + 1
                    res_l, res_r = l, r 
                l -= 1
                r += 1

            l, r = i, i + 1
            curr = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > res:
                    res = r - l + 1
                    res_l, res_r = l, r 
                l -= 1
                r += 1
            
        return s[res_l: res_r + 1]
        

