class Solution:
    def isValid(self, s: str) -> bool:
        
        map_to_c = {
            "(": ")",
            "[": "]",
            "{": "}"
        }

        stack = []
        for p in s:
            if not stack:
                stack.append(p)
            else:
                if stack and stack[-1] in map_to_c and map_to_c[stack[-1]] == p:
                    stack.pop()
                else:
                    stack.append(p)
        
        return not stack