class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if len(t) > len(s):
            return ""
        
        dict_t = Counter(t)
        have, need = 0, len(dict_t)
        window = defaultdict(int)
        l = 0
        res, resLen = [-1, -1], float("infinity")

        for r in range(len(s)):
            
            c = s[r]
            window[c] += 1

            if c in dict_t and window[c] == dict_t[c]:
                have += 1
            
            while have == need:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1

                window[s[l]] -= 1
                if s[l] in dict_t and window[s[l]] < dict_t[s[l]]:
                    have -= 1
            
                l += 1
        l, r = res
        return s[l : r + 1] if resLen != float("infinity") else ""



            
            