class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        dict_freq = defaultdict(int)
        l = 0
        res = 0

        # 6 - 4 = 2 > k 
        for r in range(len(s)):
            dict_freq[s[r]] += 1
            freq = max(dict_freq.values())
            while (r - l + 1) - freq > k:
                dict_freq[s[l]] -= 1
                l += 1
            res = max(r - l + 1, res)

        return res