class Solution:
    def trap(self, height: List[int]) -> int:
        
        # [0,2,0,3,1,0,1,3,2,1]
        #  0 2 2 3 3 3 3 3 3 3
        #  3 3 3 3 3 3 3 3 2 1

        #  0 0 2 0 2 3 2 0 0 0 -> 9

        l, r = 0, len(height) - 1
        max_l, max_r = height[l], height[r]
        res = 0

        while l <= r:
            if max_l < max_r:
                res += max_l - height[l]
                l += 1
                max_l = max(height[l], max_l)
            else:
                res += max_r - height[r]
                r -= 1
                max_r = max(height[r], max_r)
                

        return res
                
