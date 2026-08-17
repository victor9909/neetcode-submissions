class Solution:
    def rob(self, nums: List[int]) -> int:

        memo = {}

        def dp(idx, curr):

            if (idx, curr) in memo:
                return memo[(idx, curr)]

            if idx >= len(nums):
                return curr
            
            res = 0
            for i in range(idx, len(nums)):
                res = max(res, dp(i + 2, curr + nums[idx]))
            memo[(idx, curr)] = res
            return memo[(idx, curr)]

        return max(dp(0, 0), dp(1, 0))
