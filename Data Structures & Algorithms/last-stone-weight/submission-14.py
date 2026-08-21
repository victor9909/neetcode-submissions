class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            a, b = -1 * heapq.heappop(stones), -1 * heapq.heappop(stones)
            heapq.heappush(stones, -1 * abs(a-b))
        return stones[0] * -1