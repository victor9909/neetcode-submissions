class MedianFinder:

    def __init__(self):
        self.small, self.large = [], []

    def addNum(self, num: int) -> None:
        
        # Arbitrariamente aggiunto all'heap small
        heapq.heappush(self.small, -1 * num)
        # Devo mantenere la proprietà small <= large
        if self.small and self.large and -1 * self.small[0] > self.large[0]:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        # Questo è fatto per mantenere gli heap con una 
        # differenza di lunghezza al massimo di uno
        # nel caso migliore, hanno la stessa lunghezza
        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.small) + 1 < len(self.large):
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val) 

    def findMedian(self) -> float:

        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        if len(self.large) > len(self.small):
            return self.large[0]
        
        return (-1 * self.small[0] + self.large[0]) / 2




        
        