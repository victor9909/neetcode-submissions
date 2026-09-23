class Solution:
    def decodeString(self, s: str) -> str:
        
        idx = 0
        stack = []
        while idx < len(s):

            if s[idx] != "]":
                stack.append(s[idx])
                idx += 1
                continue
            
            curr_s = ""
            while s and ord("a") <= ord(stack[-1]) <= ord("z"):
                curr_s += stack.pop()
            
            curr_s = curr_s[::-1]
            stack.pop()

            curr_n = ""
            while stack and ord("0") <= ord(stack[-1]) <= ord("9"):
                curr_n += stack.pop()
            
            curr_n = int(curr_n[::-1])

            curr_s = curr_n * curr_s
            for c in curr_s:
                stack.append(c)
            idx += 1
        
        return "".join(stack)