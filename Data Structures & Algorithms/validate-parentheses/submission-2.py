class Solution:
    def isValid(self, s: str) -> bool:
        
        map_p = {
            ")": "(",
            "]": "[",
            "}": "{",
        }

        stack = []
        for p in s:
            if stack:
                if p in map_p and map_p[p] == stack[-1]:
                    stack.pop()
                else:
                    stack.append(p)
            else:
                stack.append(p)
        
        print(stack)
        return len(stack) == 0