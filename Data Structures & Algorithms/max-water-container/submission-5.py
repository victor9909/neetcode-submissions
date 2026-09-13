class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        l, r = 0, len(heights) - 1
        res = 0
        while l < r:
            height = min(heights[l], heights[r])
            area = (r - l) * height
            res = max(res, area)

            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        return res
