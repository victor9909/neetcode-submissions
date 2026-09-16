class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_ = min_ = result = nums[0]

        for n in nums[1:]:
            old_max = max_

            max_ = max(n, old_max * n, min_ * n)
            min_ = min(n, old_max * n, min_ * n)

            result = max(result, max_)

        return result