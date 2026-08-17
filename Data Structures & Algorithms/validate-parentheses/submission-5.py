class Solution:
    def isValid(self, s: str) -> bool:
        
        map_to_c = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        stack = []
        for p in s:
            if not stack:
                stack.append(p)
            else:
                if p in map_to_c and stack[-1] == map_to_c[p]:
                    stack.pop()
                else:
                    stack.append(p)
        
        return not stack