class MedianFinder:

    def __init__(self):
        self.min_h = []
        self.max_h = []

    def addNum(self, num: int) -> None:
        
        if self.max_h and num > self.max_h[0]:
            heapq.heappush(self.max_h, num)
        else:
            heapq.heappush(self.min_h, -1 * num)

        if len(self.min_h) > len(self.max_h) + 1:
            val = -1 * heapq.heappop(self.min_h)
            heapq.heappush(self.max_h, val)
        if len(self.max_h) > len(self.min_h) + 1:
            val = heapq.heappop(self.max_h)
            heapq.heappush(self.min_h, -1 * val)
        
        

    def findMedian(self) -> float:
        if len(self.min_h) > len(self.max_h):
            return -1 * self.min_h[0]
        elif len(self.max_h) > len(self.min_h):
            return self.max_h[0]
        return (-1 * self.min_h[0] + self.max_h[0]) / 2.0

        
        