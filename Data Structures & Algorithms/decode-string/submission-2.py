class Solution:
    def decodeString(self, s: str) -> str:
        
        stack = []
        for p in s:
            if not stack:
                stack.append(p)
            else:
                if stack and p == "]":
                    st = []
                    while stack and stack[-1] != "[":
                        st.append(stack.pop())
                    st = st[::-1]
                    stack.pop()
                    digit = ""
                    while stack and stack[-1].isdigit():
                        digit += stack.pop()
                    digit = int(digit[::-1])
                    stack.append("".join(st) * digit)
                    
                else:
                    stack.append(p)
        print(stack)
        return "".join(stack)