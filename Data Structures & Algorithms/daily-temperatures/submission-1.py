class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack = []
        res = [0] * len(temperatures)
        for idx, t in enumerate(temperatures):
            while stack and stack[-1][0] < t:
                tmp, i = stack.pop()
                res[i] = idx - i
            stack.append((t, idx))
        return res

        