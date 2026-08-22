class Solution:
    def rob(self, nums: List[int]) -> int:
        
        memo = {}

        def dfs(i):
            if i in memo:
                return memo[i]

            if i >= len(nums):
                return 0
            memo[i] = max(dfs(i + 2), dfs(i + 3)) + nums[i]
            return memo[i]
        
        #return max(dfs(0), dfs(1))

        dp = [0] * (len(nums) + 3)

        for i in range(len(nums) - 1, -1, -1):
            dp[i] = max(dp[i + 3], dp[i + 2]) + nums[i]
        return max(dp[0], dp[1])

