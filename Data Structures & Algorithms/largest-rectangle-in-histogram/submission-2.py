class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        stack = []
        res = 0
        for idx, h in enumerate(heights):
            start = idx
            while stack and stack[-1][1] > h:
                idx_h, hei = stack.pop()
                res = max(res, hei * (idx - idx_h))
                start = idx_h
            stack.append((start, h))
        
        for idx, h in stack:
            res = max(res, h *(len(heights) - idx))
        return res