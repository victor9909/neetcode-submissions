class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # s = "Was it a car or a cat I saw?"
        # l= 0, r = 27 -> s[l] is alpha -> Y
        #                 s[r] is alpha -> N -> r -- ->
        #                 r = 26 s[r] is alpha -> Y
        # s[0] == s[26] ? Y continue
        #               ? N return False 

        def is_alpha(c):
            return ord('A') <= ord(c) <= ord('Z') or ord('a') <= ord(c) <= ord('z') or ord('0') <= ord(c) <= ord('9')

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
