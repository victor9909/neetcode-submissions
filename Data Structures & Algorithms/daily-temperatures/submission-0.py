class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        # temperatures = [30,38,30,36,35,40,28]
        # [0,0,0,0,0,0,0] stack = []
        # idx = 0, t = 30 -> [(0, 30)]
        # idx = 1, t = 38 -> [1 (idx - idx-s),0,0,0,0,0,0] [(1, 38)]
        # idx = 2, t = 30 -> [1,0,0,0,0,0,0] [(1, 38), (2, 30)]
        # idx = 3, t = 36 -> [1,0,1,0,0,0,0] [(1, 38), (3, 36)]
        # idx = 4, t = 35 -> [1,0,1,0,0,0,0] [(1, 38), (3, 36), (4, 35)]
        # idx = 5, t = 40 -> [1,4,1,2,1,0,0] [(5, 40)]
        # idx = 6, t = 28 -> [1,4,1,2,1,0,0] [(5, 40)]

        # [1,4,1,2,1,0,0]

        stack = []
        res = [0] * len(temperatures)
        for idx, t in enumerate(temperatures):
            while stack and t > stack[-1][1]:
                stack_idx, stack_t = stack.pop()
                res[stack_idx] = idx - stack_idx
            stack.append((idx, t))
        
        return res


