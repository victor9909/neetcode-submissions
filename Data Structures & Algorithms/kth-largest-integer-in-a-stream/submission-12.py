class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.min_h = nums
        self.k = k
        heapq.heapify(self.min_h)
        while len(self.min_h) > k:
            heapq.heappop(self.min_h)

    def add(self, val: int) -> int:

        heapq.heappush(self.min_h, val)
        if self.k < len(self.min_h):
            heapq.heappop(self.min_h)

        return self.min_h[0]
        
