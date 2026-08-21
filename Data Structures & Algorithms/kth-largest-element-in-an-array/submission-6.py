class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        heap = []
        for n in nums:
            heapq.heappush(heap, n)
            if len(heap) > k:
                heapq.heappop(heap)
        res = []
        while heap:
            res.append(heapq.heappop(heap))
        
        return res[0] 
