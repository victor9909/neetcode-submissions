class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # s = "zxyzxyz" l = 0, r = 0 {}
        # s = "zxyzxyz" l = 0, r = 1 {z}
        # s = "zxyzxyz" l = 0, r = 2 {z, x}
        # s = "zxyzxyz" l = 0, r = 3 {z, x, y}
        # s = "zxyzxyz" l = 1, r = 3 {z, y}

        l, r = 0, 0
        char_set = set()
        res = 0
        while r < len(s):
            while s[r] in char_set:
                char_set.remove(s[l])
                l += 1
            char_set.add(s[r])
            res = max(res, r - l + 1)
            r += 1
        return res



        