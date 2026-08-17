class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        bit_s = [0] * 26
        bit_t = [0] * 26

        for c in s:
            bit_s[ord('z') - ord(c)] += 1
        
        for c in t:
            bit_t[ord('z') - ord(c)] += 1
        
        for i in range(26):
            if bit_s[i] != bit_t[i]:
                return False
        return True