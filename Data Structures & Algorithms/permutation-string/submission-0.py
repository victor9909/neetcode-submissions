class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        l, r = 0, len(s1) - 1

        bit_arr_s = [0] * 26
        for c in s1:
            bit_arr_s[ord('z') - ord(c)] += 1

        def is_permutation(t):
            print(t)
            bit_arr = [0] * 26
            for c in t:
                bit_arr[ord('z') - ord(c)] += 1
            
            for idx in range(26):
                if bit_arr[idx] != bit_arr_s[idx]:
                    return False
            return True

        while r < len(s2):
            
            if is_permutation(s2[l:r+1]):
                return True
            l, r = l + 1, r + 1
        
        return False