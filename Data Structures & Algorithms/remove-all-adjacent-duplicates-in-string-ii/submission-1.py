class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        
        stack = []
        for c in s:
            while stack and stack[-1][1] == k:
                stack.pop()
            count = 1
            if stack and stack[-1][0] == c:
                tmp, _c = stack.pop()
                count += _c
            stack.append((c, count))

        if stack[-1][1] == k:
            stack.pop()

        res = ""
        for char, count in stack:
            res += char * count
        return res