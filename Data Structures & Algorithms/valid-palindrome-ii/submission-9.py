class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        def is_pal(l, r):

            while l <= r:
                if s[l] != s[r]:
                    return (False, l, r)
                l += 1
                r -= 1
            return (True, None, None)
        
        l, r = 0, len(s) - 1
        is_palindrome, bl, br = is_pal(l, r)
        if is_palindrome:
            return True
        
        return is_pal(bl, br - 1)[0] or is_pal(bl + 1, br)[0]
