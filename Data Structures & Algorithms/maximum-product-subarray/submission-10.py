class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        res = nums[0]
        cur_min, cur_max = 1, 1

        for n in nums:
            tmp = cur_max * n
            cur_max = max(tmp, cur_min * n, n)
            cur_min = min(tmp, n, n * cur_min)

            res = max(res, cur_max)
        
        return res