class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # s = "zxyzxyz" {} l = 0 r = 0 max_p = [l, r] max_l = 0 
        # z is in {} ? No -> {z} r+= 1
        # x is in {z} ? NO {x, z} r+= 1
        # y is in {x, z} ? No {x, y, z} r += 1
        # z is in {x, y, z} ? Yes max_l = 3 max_p = [0, 3]
        # l += 1 remove from {x, y} -> r = 4 {x, y, z}


        l, r = 0, 0
        visit_set = set()
        res= 0
        while r < len(s):
            while s[r] in visit_set:
                visit_set.remove(s[l])
                l += 1
            visit_set.add(s[r])
            res = max(res, r - l + 1)
            r += 1
        return res
