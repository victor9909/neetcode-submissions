class MinStack:

    def __init__(self):
        self.stack = []
        self.min_val = None

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.min_val = min(self.stack)

    def pop(self) -> None:
        self.stack.pop()
        self.min_val = min(self.stack) if self.stack else None

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_val
        
