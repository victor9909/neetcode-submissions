class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        dict_s, dict_t = Counter(s), Counter(t)
        for k in dict_s:
            if k not in dict_t:
                return False
            if k in dict_t and dict_s[k] != dict_t.get(k, 0):
                return False
        return True