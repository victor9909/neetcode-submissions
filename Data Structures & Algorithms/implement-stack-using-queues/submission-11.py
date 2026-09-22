class MyStack:

    def __init__(self):
        self.q1, self.q2 = deque(), deque()

    def push(self, x: int) -> None:
        self.q1.append(x)

    def pop(self) -> int:
        
        while self.q1:
            self.q2.appendleft(self.q1.popleft())

        return self.q2.popleft()

    def top(self) -> int:
        return self.q1[-1] if self.q1 else self.q2[0]

    def empty(self) -> bool:
        return not self.q1 and not self.q2


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()