class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        memo = {}
        def dfs(i):
            if i in memo:
                return memo[i]
            if i >= len(nums):
                return 0
            
            res = 0
            for j in range(i + 1, len(nums)):
                if nums[i] >= nums[j]:
                    continue
                res = max(res, 1 + dfs(j))
            memo[i] = res
            return res
        
        #res = 0
        #for i in range(len(nums)):
        #    res = max(res, dfs(i) + 1)

        dp = [0] * (len(nums) + 1)
        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] >= nums[j]:
                    continue
                dp[i] = max(dp[i], 1 + dp[j])

        return max(dp) + 1

