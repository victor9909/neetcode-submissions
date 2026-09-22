class Solution:
    def decodeString(self, s: str) -> str:

        stack = []

        for c in s:

            if c != "]":
                stack.append(c)
                continue

            curr_s = ""

            while stack[-1] != "[":
                curr_s += stack.pop()

            stack.pop()  # remove "["

            num = ""

            while stack and stack[-1].isdigit():
                num += stack.pop()

            num = num[::-1]

            decoded = int(num) * curr_s[::-1]

            for char in decoded:
                stack.append(char)

        return "".join(stack)