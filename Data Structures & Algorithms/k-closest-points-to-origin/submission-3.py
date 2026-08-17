class Point:

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.diff_neg = math.sqrt((x ** 2) + (y ** 2)) * -1
    
    def __lt__(self, other: Point):
        return self.diff_neg < other.diff_neg

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        heap = [Point(x, y) for x, y in points]
        heapq.heapify(heap)
        while len(heap) > k:
            heapq.heappop(heap)
        
        return [[p.x, p.y] for p in heap]
