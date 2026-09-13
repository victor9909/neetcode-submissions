class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        res = float("inf")
        res_idx = [-1, -1]

        l = 0
        
        window_t = Counter(t)
        window_r = defaultdict(int)
        have, need = 0, len(window_t)

        for r in range(len(s)):

            c = s[r]
            window_r[c] += 1

            if c in window_t and window_r[c] == window_t[c]:
                have += 1
            
            while have == need:
                if r - l + 1 < res:
                    res = r - l + 1
                    res_idx = [l, r]
                
                window_r[s[l]] -= 1
                if s[l] in window_t and window_r[s[l]] < window_t[s[l]]:
                    have -= 1
                l += 1
        
        l, r = res_idx
        return s[l: r + 1] if res != float("inf") else ""



            


