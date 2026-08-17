class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s2) < len(s1):
            return False
        
        l = 0
        bit_s1 = [0] * 26
        for c in s1:
            bit_s1[ord('z') - ord(c)] += 1

        bit_s2 = [0] * 26
        for r in range(len(s2)):

            if r < len(s1):
                bit_s2[ord('z') - ord(s2[r])] += 1
                continue
            
            if bit_s1 == bit_s2:
                return True
            
            bit_s2[ord('z') - ord(s2[r])] += 1
            bit_s2[ord('z') - ord(s2[l])] -= 1
            l += 1
        
        return bit_s1 == bit_s2

