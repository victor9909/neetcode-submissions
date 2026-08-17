class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        l, res, char_set = 0, 0, set()

        for r in range(len(s)):
            while s[r] in char_set:
                char_set.remove(s[l])
                l += 1
            char_set.add(s[r])
            res = max(res, (r - l + 1))
        return res