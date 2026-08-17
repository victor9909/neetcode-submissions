class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        def build_bit_arr(s):
            bit = [0] * 26
            for c in s:
                bit[ord('z') - ord(c)] += 1
            return bit
        
        bit_s = build_bit_arr(s)
        bit_t = build_bit_arr(t)
        
        for i in range(26):
            if bit_s[i] != bit_t[i]:
                return False
        
        return True
        