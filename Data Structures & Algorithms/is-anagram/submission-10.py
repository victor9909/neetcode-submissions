class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        dict_t, dict_s = Counter(s), Counter(t)
        for k in dict_s:
            if dict_s[k] != dict_t.get(k, 0):
                return False
        return True
