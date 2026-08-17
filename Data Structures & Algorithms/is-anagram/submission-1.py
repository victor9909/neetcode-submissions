class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
            
        bit_arr = [0] * 26

        for c in s:
            bit_arr[ord('z') - ord(c)] += 1
        
        for c in t:
            bit_arr[ord('z') - ord(c)] -= 1
            if bit_arr[ord('z') - ord(c)] < 0:
                return False
        
        return True