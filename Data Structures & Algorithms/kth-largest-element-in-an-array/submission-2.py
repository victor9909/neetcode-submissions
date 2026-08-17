class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        heapq.heapify(nums)
        
        res = []
        while nums:
            res.append(heapq.heappop(nums))

        return res[len(res) - k]
