class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        
        def is_pal(l, r, flag):
        
            while l < r:
                
                if s[l] != s[r] and flag:
                    return False
                elif s[l] != s[r] and not flag:
                    return is_pal(l, r - 1, True) or is_pal(l + 1, r, True)
                
                l += 1
                r -= 1

            return True
        
        return is_pal(0, len(s) - 1, False)

        

            