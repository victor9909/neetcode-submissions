class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        curr_str = ""
        curr_num = 0

        for c in s:
            if c.isdigit():
                curr_num = curr_num * 10 + int(c)  # gestisce multi-cifra
            elif c == "[":
                stack.append((curr_str, curr_num))  # salva stato corrente
                curr_str = ""
                curr_num = 0
            elif c == "]":
                prev_str, num = stack.pop()
                curr_str = prev_str + num * curr_str  # ricostruisce
            else:
                curr_str += c

        return curr_str

        
            
