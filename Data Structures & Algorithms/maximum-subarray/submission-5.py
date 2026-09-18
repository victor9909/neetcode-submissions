class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        curr = nums[0]
        max_res = nums[0]
        for n in nums[1:]:
            max_res = max(max_res, curr + n, n)
            curr = max(n, curr + n)
        return max_res