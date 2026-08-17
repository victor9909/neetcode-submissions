class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        bit_arr_s = [0] * 26
        bit_arr_t = [0] * 26

        for c in s:
            bit_arr_s[ord('z') - ord(c)] += 1
        for c in t:
            bit_arr_t[ord('z') - ord(c)] += 1
        
        for idx in range(26):
            if bit_arr_s != bit_arr_t:
                return False
        return True
