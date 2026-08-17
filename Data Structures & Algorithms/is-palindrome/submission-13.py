class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        def is_alpha_num(c):
            is_upp = ord('A') <= ord(c) <= ord('Z')
            is_low = ord('a') <= ord(c) <= ord('z')
            is_digit = ord('0') <= ord(c) <= ord('9')
            return is_upp or is_low or is_digit
        
        l, r = 0, len(s) - 1
        while l < r:
            
            while l < r and not is_alpha_num(s[l]):
                l += 1
            
            while l < r and not is_alpha_num(s[r]):
                r -= 1
            
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1

        return True