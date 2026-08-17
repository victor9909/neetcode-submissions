class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        memo = {len(nums):0}

        def dpf(i: int):

            if i in memo:
                return memo[i]

            if i >= len(nums):
                return 0
            
            res = 1
            for j in range(i + 1, len(nums)):
                if nums[i] >= nums[j]:
                    continue
                res = max(dpf(j) + 1, res)
            
            memo[i] = res
            return memo[i]
        
        #res = 0
        #for i in range(len(nums)):
        #    curr = dpf(i)
        #    res = max(res, curr)

        #return res

        dp = [1] * (len(nums))
        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[j] <= nums[i]:
                    continue
                dp[i] = max(dp[j] + 1, dp[i])

        return max(dp)


