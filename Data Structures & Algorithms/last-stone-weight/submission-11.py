class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        stones = [-w for w in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first = heapq.heappop(stones) * -1
            second = heapq.heappop(stones) *-1

            stone = first - second
            heapq.heappush(stones, stone * -1)

        return stones[0] * -1
