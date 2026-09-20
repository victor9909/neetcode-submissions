class Solution:

    class Point:

        def __init__(self, x, y):
            self.x = x
            self.y = y
            self.dist = ((x ** 2) + (y ** 2)) ** 0.5
        
        def __lt__(self, other):
            return self.dist > other.dist

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        min_h = [self.Point(x, y) for x, y in points]
        heapq.heapify(min_h)

        while len(min_h) > k:
            heapq.heappop(min_h)

        return [[p.x, p.y] for p in min_h]
