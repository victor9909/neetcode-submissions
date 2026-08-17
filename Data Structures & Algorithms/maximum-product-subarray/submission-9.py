class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        curr = nums[0]
        curr_min, curr_max = nums[0], nums[0]
        res = nums[0]

        for n in nums[1:]:
            tmp_min, tmp_max = curr_min, curr_max
            curr_min = min(n, curr_min * n, tmp_max * n)
            curr_max = max(n, curr_max * n, tmp_min * n)
            res = max(curr_max, res)
        
        return res