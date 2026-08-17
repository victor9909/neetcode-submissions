class Solution:
    def rob(self, nums: List[int]) -> int:

        memo = {}

        def dp(idx):
            
            if idx in memo:
                return memo[idx]

            if idx >= len(nums):
                return 0
            
            memo[idx] = max(
                nums[idx] + dp(idx + 2),
                dp(idx + 1)
            )

            return memo[idx]

        #return dp(0)

        if len(nums) < 3:
            first = nums[0]
            second = nums[1] if len(nums) == 2 else 0
            return max(first, second)

        dp = [0] * (len(nums) + 1)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for idx in range(len(nums)):
            dp[idx] = max(nums[idx] + dp[idx - 2], dp[idx - 1])
        
        return dp[-2]


