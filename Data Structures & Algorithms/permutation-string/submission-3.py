class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        l = 0
        r = 0
        len_s1 = len(s1)
        
        bit_arr = [0] * 26
        for c in s1:
            bit_arr[ord("z") - ord(c)] += 1
        
        bit_arr_s = [0] * 26
        for r in range(len(s2)):

            bit_arr_s[ord("z") - ord(s2[r])] += 1
            if (r - l + 1) < len_s1:
                continue
            
            if bit_arr_s == bit_arr:
                return True
            
            bit_arr_s[ord("z") - ord(s2[l])] -= 1
            l += 1
        
        return False
            
