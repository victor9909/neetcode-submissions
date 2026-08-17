class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s2) < len(s1):
            return False

        dict_s1 = Counter(s1)
        dict_s2 = defaultdict(int)
        
        l = 0
        for r in range(len(s2)):
            dict_s2[s2[r]] += 1
            if r - l + 1 < len(s1):
                continue

            print(dict_s1, dict_s2)
            if dict_s1 == dict_s2:
                return True
            
            dict_s2[s2[l]] -= 1
            if dict_s2[s2[l]] == 0:
                del dict_s2[s2[l]]
            l += 1
        
        return False




