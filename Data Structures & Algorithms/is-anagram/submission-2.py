class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        bit_arr_s = [0] * 26
        for c in s:
            bit_arr_s[ord('z') - ord(c)] += 1
        
        bit_arr_t = [0] * 26
        for c in t:
            bit_arr_t[ord('z') - ord(c)] += 1
        
        for i in range(26):
            if bit_arr_s[i] != bit_arr_t[i]:
                return False
        
        return True
    
        
        