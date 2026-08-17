class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        res_l, res_r = 0, 0
        max_l = float("-inf")

        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:

                if s[l] == s[r]:
                    if (r - l + 1) > max_l:
                        max_l = (r - l + 1)
                        res_l = l
                        res_r = r

                    l = l - 1
                    r = r + 1
            
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:

                if s[l] == s[r]:
                    if (r - l + 1) > max_l:
                        max_l = (r - l + 1)
                        res_l = l
                        res_r = r

                    l = l - 1
                    r = r + 1
        
        return s[res_l:res_r+1]

