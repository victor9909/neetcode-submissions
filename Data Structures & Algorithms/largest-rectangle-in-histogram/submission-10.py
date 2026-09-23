class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        stack = []
        res = 0
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                idx, height = stack.pop()
                start = idx
                res = max(res, (i - idx) * height)
            stack.append((start, h))
        
        print(stack)
        for i, h in stack:
            res = max(res, (len(heights) - i) * h)
        return res
