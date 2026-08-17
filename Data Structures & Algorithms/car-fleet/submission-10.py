class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        stack = []
        arr = [(p, s) for p, s in zip(position, speed)]
        arr.sort(key = lambda x: x[0])

        for p, s in arr:
            time = (target - p) / s
            while stack and stack[-1] <= time:
                stack.pop()
            stack.append(time)
        return len(stack)