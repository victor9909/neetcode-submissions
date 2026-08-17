class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        dict_freq = set()
        l = 0
        res = 0
        for r in range(len(s)):
            while s[r] in dict_freq:
                dict_freq.remove(s[l])
                l += 1
            res = max(res, r - l + 1)
            dict_freq.add(s[r])
        return res
