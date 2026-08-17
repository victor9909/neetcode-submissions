class Solution:
    def rob(self, nums: List[int]) -> int:
        
        memo = {}

        def dpf(i: int):

            if i in memo:
                return memo[i]

            if i >= len(nums):
                return 0
            
            memo[i] = max(dpf(i+2), dpf(i+3)) + nums[i]
            return memo[i]
        
        #return max(dpf(0), dpf(1))

        if len(nums) <= 2:
            return max(nums)

        dp = [0] * (len(nums) + 1)
        dp[-2] = nums[-1]
        dp[-3] = nums[-2]

        for i in range(len(nums) - 3, -1, -1):
            dp[i] = max(dp[i + 2], dp[i + 3]) + nums[i]
        
        return max(dp[0], dp[1])

        

        