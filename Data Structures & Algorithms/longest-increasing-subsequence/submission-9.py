class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        memo = {}

        def dpf(i: int):

            if i >= len(nums):
                return 0
            
            if i in memo:
                return memo[i]

            res = 1
            for j in range(i+1, len(nums)):
                if nums[j] <= nums[i]:
                    continue
                res = max(res, 1 + dpf(j))
            memo[i] = res
            return res
        
        res = 0
        for i in range(len(nums)):
            res = max(res, dpf(i))

        return res
