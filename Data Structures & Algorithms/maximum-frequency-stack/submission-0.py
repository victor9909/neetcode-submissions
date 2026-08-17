class FreqStack:

    def __init__(self):
        self.cnt = defaultdict(int)
        self.max_c = 0
        self.stack = {}

    def push(self, val: int) -> None:
        val_c = self.cnt[val] + 1
        self.cnt[val] = val_c
        if val_c > self.max_c:
            self.max_c = val_c
            self.stack[val_c] = []
        self.stack[val_c].append(val)

    def pop(self) -> int:
        val = self.stack[self.max_c].pop()
        self.cnt[val] -= 1
        if not self.stack[self.max_c]:
            self.max_c -= 1
        return val

        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()