class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        # 2,3,1,5,4
        # 1, 2, 3, 4, 5
        
        min_h = [n for n in nums]
        heapq.heapify(min_h)

        while len(min_h) > k:
            heapq.heappop(min_h)
        
        return min_h[0]