class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        map_dict = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        stack = []
        for p in s:
            if stack:
                if p in map_dict and stack[-1] == map_dict[p]:
                    stack.pop()
                else:
                    stack.append(p)
            else:
                stack.append(p)
        
        return not stack