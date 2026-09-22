class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        def is_neg(a):
            return a < 0
        
        def is_pos(a):
            return a > 0
        
        stack = []
        for a in asteroids:
            if not stack:
                stack.append(a)
            else:

                while stack and is_pos(stack[-1]) and is_neg(a):
                    if abs(stack[-1]) > abs(a):
                        break
                    elif abs(stack[-1]) < abs(a):
                        stack.pop()
                    else:
                        stack.pop()
                        break
                else:
                    stack.append(a)
                

        return stack



