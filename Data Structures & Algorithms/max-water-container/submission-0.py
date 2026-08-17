class Solution:
    def maxArea(self, heights: List[int]) -> int:

        # height = [1,7,2,5,4,7,3,6]
        # l = 0, r = 8 -> area = 1 * 7 = 7 max_area = 36
        # l = 1, r = 8 -> area = 6 * 6 = 36 max_area = 36
        # l = 1, r = 7 -> area = 3 * 5 = 15 max_area = 36
        # ...

        l, r = 0, len(heights) - 1
        max_area = 0
        while l < r:
            curr_area = min(heights[l], heights[r]) * (r - l)
            max_area = max(max_area, curr_area)
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        
        return max_area


        