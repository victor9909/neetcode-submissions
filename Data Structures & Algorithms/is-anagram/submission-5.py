class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        map_a = {}

        for c in s:
            map_a[c] = map_a.get(c, 0) + 1

        for c in t:
            if c not in map_a:
                return False
            map_a[c] -= 1
            if map_a[c] == 0:
                del map_a[c]
        return True
        
        

        