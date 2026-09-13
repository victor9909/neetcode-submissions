class Solution:
    def isValid(self, s: str) -> bool:
        
        map_to_c = {
            "}": "{",
            "]": "[",
            ")": "("
        }

        stack = []
        for c in s:
            if not stack:
                stack.append(c)
            else:
                if c in map_to_c and stack[-1] == map_to_c[c]:
                    stack.pop()
                else:
                    stack.append(c)
        return not stack