class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        ps = [(p, s) for p, s in zip(position, speed)]
        ps.sort()
        stack = []

        # [4,1,0,7]
        #  2,2,1,1]

        #(4,2) (1,2) (0,1) (7,1)
        # (0,1)(1,2)(4,2)(7,1)

        # (7,1)(4,2)(1,2)(0,1)
        # 3 4.5 10 

        # [0,4,2]
        # [2,1,3]

        

        for p, s in ps:
            t = (target - p) / s
            while stack and stack[-1] <= t:
                stack.pop()
            stack.append(t)
        return len(stack)

