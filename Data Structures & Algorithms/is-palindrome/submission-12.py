class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        def is_alphanum(c):
            is_lower = ord('a') <= ord(c) <= ord('z')
            is_upper = ord('A') <= ord(c) <= ord('Z')
            is_digit = ord('0') <= ord(c) <= ord('9')
            return is_lower or is_upper or is_digit

        l, r = 0, len(s) - 1
        while l <= r:

            while l < r and l < len(s) and not is_alphanum(s[l]):
                l += 1
            
            while l < r and r > 0 and not is_alphanum(s[r]):
                r -= 1

            if s[l].lower() != s[r].lower():
                return False
            
            l += 1
            r -= 1

        return True

