class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        def is_alpha(c):
            is_num = ord('0') <= ord(c) <= ord('9')
            is_upper = ord('A') <= ord(c) <= ord('Z')
            is_lower = ord('a') <= ord(c) <= ord('z')
            return is_num or is_upper or is_lower
        
        l, r = 0, len(s) - 1
        while l < r:
            
            while l < r and not is_alpha(s[l]):
                l += 1
            while l < r and not is_alpha(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            
            l += 1
            r -= 1

        return True