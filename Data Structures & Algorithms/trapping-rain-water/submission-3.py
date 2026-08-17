class Solution:
    def trap(self, height: List[int]) -> int:
        
        max_l, max_r = [], []
        curr = 0
        for h in height:
            max_l.append(curr)
            curr = max(h, curr)
        
        curr = 0
        for h in height[::-1]:
            max_r.append(curr)
            curr = max(h, curr)
        max_r = max_r[::-1]
        
        res = 0
        for i, h in enumerate(height):
            curr = min(max_l[i], max_r[i]) - h
            res += curr if curr > 0 else 0
        return res
