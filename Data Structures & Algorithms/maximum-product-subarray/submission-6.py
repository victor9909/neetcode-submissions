class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        res = nums[0]
        curr_min, curr_max = 1, 1

        for n in nums:
            tmp = n * curr_max
            curr_max = max(tmp, n, n * curr_min)
            curr_min = min(tmp, n, n * curr_min)
            res = max(res, curr_max, curr_min)
        
        return res
