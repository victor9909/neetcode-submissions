class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        lenght = 0
        l_max, r_max = 0, 0

        for i, c in enumerate(s):

            # odd length
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > lenght:
                    lenght = r - l + 1
                    l_max = l
                    r_max = r
                l -= 1
                r += 1
            
            # even length
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > lenght:
                    lenght = r - l + 1
                    l_max = l
                    r_max = r
                l -= 1
                r += 1
            
        return s[l_max: r_max + 1]

