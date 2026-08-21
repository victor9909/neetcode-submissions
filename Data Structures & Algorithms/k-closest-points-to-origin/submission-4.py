class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        min_heap = []
        for x, y in points:
            dist = x ** 2 + y ** 2
            heapq.heappush(min_heap, (-1 * dist, x, y))
        
        while len(min_heap) > k:
            heapq.heappop(min_heap)
        
        return [(x, y) for _, x, y in min_heap]
        