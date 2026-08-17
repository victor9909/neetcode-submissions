class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        

        time = [(p, s) for p, s in zip(position, speed)]
        time.sort()
        stack = []
        for p,s in time[::-1]:
            tmp = (target - p) / s
            if stack and stack[-1] < tmp:
                stack.append(tmp)
            else:
                if not stack:
                    stack.append(tmp)
        
        return len(stack)