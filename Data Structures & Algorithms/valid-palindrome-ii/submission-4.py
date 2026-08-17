class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        def is_alpha(c):
            is_upp = ord('A') <= ord(c) <= ord('Z')
            is_low = ord('a') <= ord(c) <= ord('z')
            is_num = ord('0') <= ord(c) <= ord('9')
            return is_upp or is_low or is_num

        def is_pal(l, r):

            while l <= r:

                while l < r and not is_alpha(s[l]):
                    l += 1
                
                while l < r and not is_alpha(s[r]):
                    r -= 1
                
                if s[l].lower() != s[r].lower():
                    return (False, (l, r))
                
                l += 1
                r -= 1
            
            return (True, (0, 0))
            
        l, r = 0, len(s) - 1
        pal, (l, r) = is_pal(l, r)
        if not pal:
            return is_pal(l + 1, r)[0] or is_pal(l, r - 1)[0]
        
        return True


        
        