class Solution:
    def isValid(self, s: str) -> bool:
        
        map_c_o = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
        
        stack = []
        for p in s:
            if stack and p in map_c_o:
                if map_c_o[p] == stack[-1]:
                    stack.pop()
                else:
                    stack.append(p)
            else:
                stack.append(p)
        
        return not stack
                