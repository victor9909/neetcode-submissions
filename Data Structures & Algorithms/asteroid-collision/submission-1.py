from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        stack = []

        for asteroid in asteroids:
            destroyed = False

            while stack and asteroid < 0 < stack[-1]:  # unica combo che collide
                if stack[-1] < abs(asteroid):
                    stack.pop()         # il top esplode, il nuovo continua
                    continue
                elif stack[-1] == abs(asteroid):
                    stack.pop()         # entrambi esplodono
                destroyed = True        # il nuovo asteroide è distrutto
                break

            if not destroyed:
                stack.append(asteroid)

        return stack