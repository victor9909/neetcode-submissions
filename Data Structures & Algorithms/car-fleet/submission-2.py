class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        # target = 10, position = [1,4], speed = [3,2]
        # [(1, 3), (4, 2)] -> [3, 3] -> 1

        # target = 10, position = [4,1,0,7], speed = [2,2,1,1]
        # [(4, 2), (1, 2), (0, 1), (7, 1)] -> [3, 4.5, 9, 3]

        # target=12 position=[10,8,0,5,3] speed=[2,4,1,1,3]
        # [(10, 2), (8, 4), (0, 1), (5, 1), (3, 3)] -> [1, 1, 12, 7, 3]

        time = [(p, s) for p, s in zip(position, speed)]
        time.sort(reverse=True)
        stack = []
        for p,s in time:
            tmp = (target - p) / s
            if stack and stack[-1] < tmp:
                stack.append(tmp)
            else:
                if not stack:
                    stack.append(tmp)
        
        return len(stack)