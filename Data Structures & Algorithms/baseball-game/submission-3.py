class Solution:
    def calPoints(self, operations: List[str]) -> int:
        
        stack = []
        for op in operations:
            if op == "+":
                a, b = stack[-1], stack[-2]
                stack.append(a + b)
            elif op == "D":
                a = stack[-1]
                stack.append(a * 2)
            elif op == "C":
                stack.pop()
            else:
                stack.append(int(op))
        
        print(stack)
        return sum(stack)