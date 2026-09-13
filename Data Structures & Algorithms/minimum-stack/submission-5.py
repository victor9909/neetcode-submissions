class MinStack:

    def __init__(self):
        self.s = []
        self.min_s = []

    def push(self, val: int) -> None:
        self.s.append(val)
        min_v = min(self.min_s[-1], val) if self.min_s else val
        self.min_s.append(min_v)

    def pop(self) -> None:
        self.min_s.pop()
        self.s.pop()

    def top(self) -> int:
        return self.s[-1]

    def getMin(self) -> int:
        return self.min_s[-1]
