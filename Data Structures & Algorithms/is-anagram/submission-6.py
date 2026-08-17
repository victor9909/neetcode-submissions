class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        bit_a = [0] * 26
        bit_b = [0] * 26

        for c in s:
            bit_a[ord('z') - ord(c)] += 1
        
        for c in t:
            bit_b[ord('z') - ord(c)] += 1
        
        for i in range(26):
            if bit_a[i] != bit_b[i]:
                return False
        return True