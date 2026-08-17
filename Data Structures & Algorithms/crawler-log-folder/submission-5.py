class Solution:
    def minOperations(self, logs: List[str]) -> int:
        
        
        stack = []
        for l in logs:
            if l == "../" and stack:
                stack.pop()
            elif l == "./":
                continue
            else:
                if l != "../" and l != "./":
                    stack.append(l)
        
        return len(stack)