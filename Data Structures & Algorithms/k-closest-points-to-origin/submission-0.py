class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        points = [(-math.sqrt(pow(x, 2) + pow(y, 2)), x, y) for x,y in points]
        heapq.heapify(points)

        while len(points) > k:
            heapq.heappop(points)

        return [[x, y] for dist, x, y in points]