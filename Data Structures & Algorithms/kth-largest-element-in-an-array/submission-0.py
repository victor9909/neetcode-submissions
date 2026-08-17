class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        heapq.heapify(nums)
        sorted_nums = [heapq.heappop(nums) for _ in range(len(nums))]
        return sorted_nums[len(sorted_nums) - k]