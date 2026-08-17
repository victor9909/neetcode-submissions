class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_prod = nums[0]
        min_p, max_p = 1, 1

        for n in nums:
            tmp = max_p * n
            max_p = max(tmp, n * min_p, n)
            min_p = min(tmp, n * min_p, n)
            max_prod = max(max_p, max_prod)

        return max_prod