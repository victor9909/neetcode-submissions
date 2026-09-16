class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        max_l = float("-inf")
        lr, rr = -1, -1

        for i in range(len(s)):

            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > max_l:
                    max_l = r - l + 1
                    lr, rr = l, r
                l -= 1
                r += 1
            
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > max_l:
                    max_l = r - l + 1
                    lr, rr = l, r
                l -= 1
                r += 1
        
        return s[lr:rr+1] if max_l != float("-inf") else ""
            
