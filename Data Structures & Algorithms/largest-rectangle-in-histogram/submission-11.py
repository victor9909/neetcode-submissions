class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        res, stack = 0, []

        for idx, height in enumerate(heights):
            start = idx
            while stack and stack[-1][1] > height:
                i, h = stack.pop()
                res = max(res, (idx - i) * h)
                start = i
            stack.append((start, height))
        
        for i, h in stack:
            res = max(res, (len(heights) - i) * h)
        return res