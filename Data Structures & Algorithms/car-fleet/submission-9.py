class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        zipped = [(p, s) for p, s in zip(position, speed)]
        zipped.sort()

        # (1, 4) (3, 2)
        # 2,25 3,5 -> 1
 
        # (4, 2) (1, 2) (0, 1) (7, 1)
        # (0, 1) (1, 2) (4, 2) (7, 1)

        # 10 4,5 3 -> 3

        stack = []
        for p, s in zipped:
            time = (target - p) / s
            while stack and stack[-1] <= time:
                stack.pop()
            stack.append(time)
        
        return len(stack)
