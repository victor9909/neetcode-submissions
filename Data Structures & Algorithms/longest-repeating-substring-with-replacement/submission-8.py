class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        dict_freq = defaultdict(int)
        max_f = 0
        l = 0
        res = 0

        for r in range(len(s)):
            dict_freq[s[r]] += 1
            max_f = max(dict_freq.values())
            while r - l + 1 - max_f > k:
                dict_freq[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res
