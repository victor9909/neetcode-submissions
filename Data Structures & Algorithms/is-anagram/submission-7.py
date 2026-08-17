class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        counts = Counter(s)
        countt = Counter(t)
        for c in s:
            if counts[c] != countt.get(c, 0):
                return False
        
        return True