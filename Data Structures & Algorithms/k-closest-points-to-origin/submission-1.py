class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        dist = [[-1 * (x * x + y * y), [x, y]] for x, y in points]
        heapq.heapify(dist)

        while len(dist) > k:
            heapq.heappop(dist)
        
        res = [point[1] for point in dist]
        return res
