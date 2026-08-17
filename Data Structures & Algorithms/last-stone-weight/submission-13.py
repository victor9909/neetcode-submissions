class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        stones = [-w for w in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            a, b = heapq.heappop(stones), heapq.heappop(stones)
            if abs(a) != abs(b):
                diff = abs(a) - abs(b) if abs(a) > abs(b) else abs(b) - abs(a)
                heapq.heappush(stones, diff * - 1)
        
        return stones[0] * -1 if stones else 0