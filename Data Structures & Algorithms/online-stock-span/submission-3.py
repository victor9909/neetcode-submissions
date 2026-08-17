class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:

        # [100], [80], [60], [70], [60], [75], [85]
        # 100, 1
        # 100, 1 -> 80, 1
        # 100, 1 -> 80, 1 -> 60, 1
        # 100, 1 -> 80, 1 -> 70, 2
        # 100, 1 -> 80, 1 -> 70, 2 -> 60, 1
        # 100, 1 -> 80, 1 -> 75, 4  
        # 100, 1 -> 85, 6
        
        span = 1
        while self.stack and self.stack[-1][0] <= price:
            _, tmp = self.stack.pop()
            span = span + tmp
        self.stack.append((price, span))
        return span
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)