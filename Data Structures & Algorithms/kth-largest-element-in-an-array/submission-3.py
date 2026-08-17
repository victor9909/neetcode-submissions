class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        heapq.heapify(nums)
        n = len(nums) - k + 1
        res = 0

        while n > 0:
            res = heapq.heappop(nums)
            n -= 1
        
        return res
