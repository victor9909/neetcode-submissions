class Solution:
    def trap(self, height: List[int]) -> int:
        
        l, r = 0, len(height) - 1
        max_l, max_r = height[l], height[r]
        res = 0

        while l < r:
            if max_l < max_r:
                l += 1
                max_l = max(max_l, height[l])
                curr = max_l - height[l]
                res += curr
                
                
            else:
                r -= 1
                max_r = max(max_r, height[r])
                curr = max_r - height[r]
                res += curr
                
                
        return res
