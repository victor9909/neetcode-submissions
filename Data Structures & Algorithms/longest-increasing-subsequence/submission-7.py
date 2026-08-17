class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        def dpf(i):

            if i >= len(nums):
                return 0
            
            res = 1
            for j in range(i + 1, len(nums)):
                if nums[i] >= nums[j]:
                    continue
                res = max(res, dpf(j) + 1)
            return res
        
        #res = 0
        #for i in range(len(nums)):
        #    res = max(res, dpf(i))

        #return res

        dp = [1] * (len(nums) + 1)
        dp[len(nums)] = 0

        for i in range(len(nums), -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])
        return max(dp)
                

