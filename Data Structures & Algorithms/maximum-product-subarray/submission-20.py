class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_ = min_ = result = nums[0]

        for n in nums[1:]:

            max_, min_ = max(n, max_ * n, min_ * n), min(n, max_ * n, min_ * n)

            result = max(result, max_)

        return result