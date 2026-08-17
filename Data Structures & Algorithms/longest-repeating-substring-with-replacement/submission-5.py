class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_set = {}
        l, r = 0, 0
        maxf = 0
        res = 0
        while r < len(s):
            char_set[s[r]] = char_set.get(s[r], 0) + 1
            maxf = max(maxf, char_set[s[r]])
            while (r - l + 1) - maxf > k:
                char_set[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
            r += 1

        return res