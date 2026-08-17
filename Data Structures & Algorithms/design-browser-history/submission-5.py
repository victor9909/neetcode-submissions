class BrowserHistory:

    def __init__(self, homepage: str):
        self.stack = [homepage]
        self.stack_last = []

    def visit(self, url: str) -> None:
        self.stack.append(url)
        self.stack_last = []

    def back(self, steps: int) -> str:
        for s in range(steps):
            if len(self.stack) > 1:
                url = self.stack.pop()
                print(url)
                self.stack_last.append(url)
        return self.stack[-1]

    def forward(self, steps: int) -> str:
        for s in range(steps):
            if len(self.stack_last) > 0:
                url = self.stack_last.pop()
                print(url)
                self.stack.append(url)
        return self.stack[-1]
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)