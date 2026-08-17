class MinStack:

    def __init__(self):
        self.min_s = []
        self.stack = []

    def push(self, val: int) -> None:
        min_v = min(val, self.min_s[-1]) if self.min_s else val
        self.min_s.append(min_v)
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.min_s.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_s[-1]
        
