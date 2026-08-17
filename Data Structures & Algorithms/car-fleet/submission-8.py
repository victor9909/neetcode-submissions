class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        # [4,1,0,7] [2,2,1,1] -> [(4, 2),(1, 2),(0, 1),(7, 1)]
        # [(0, 1), (1, 2), (4, 2), (7, 1)] target = 10
        # [ (7, 1), (4, 2), (1, 2), (0, 1)]
        # [(3, 3), 4.5, 10]

        zipped = [(p, s) for p, s in zip(position, speed)]
        zipped.sort()
        stack = []

        for p, s in zipped[::-1]:
            v = (target-p)/s
            if not stack or v > stack[-1]:
                stack.append(v)
        return len(stack)
