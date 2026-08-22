class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        max_c, min_c = 1, 1
        curr = 1
        res = float("-inf")
        for n in nums:
            tmp = max_c * n
            max_c = max(n, tmp, min_c * n)
            min_c = min(n, tmp, min_c * n)
            res = max(res, max_c)
        return res
