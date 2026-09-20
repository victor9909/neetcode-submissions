class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        max_h = [-s for s in stones]
        heapq.heapify(max_h)

        while len(max_h) > 1:
            a, b = -1 * heapq.heappop(max_h), -1 * heapq.heappop(max_h)
            if a != b:
                heapq.heappush(max_h, -1 * abs(a - b))
            
        return -1 * max_h[0] if max_h else 0