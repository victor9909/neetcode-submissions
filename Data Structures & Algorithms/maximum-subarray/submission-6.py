class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        curr = nums[0]
        max_res = nums[0]
        for n in nums[1:]:
            curr = max(n, curr + n)
            max_res = max(max_res, curr)
        return max_res