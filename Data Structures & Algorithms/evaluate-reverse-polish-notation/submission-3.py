class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        # tokens = ["1","2","+","3","*","4","-"]
        stack = []

        for t in tokens:
            if t == "+":
                a, b = stack.pop(), stack.pop()
                stack.append(a + b)
            elif t == "*":
                a, b = stack.pop(), stack.pop()
                stack.append(a * b)
            elif t == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif t == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(b / a))
            else:
                stack.append(int(t))
        
        return stack[-1]