class Solution:
    def jump(self, nums: List[int]) -> int:
        
        memo = {}

        def dfs(i):

            if i in memo:
                return memo[i]

            if i >= len(nums) - 1:
                return 0
            
            res = float("inf")
            for j in range(nums[i]):
                res = min(res, dfs(i + j + 1) + 1)
            memo[i] = res
            return res
        
        #return dfs(0)

        dp = [float("inf")] * len(nums)
        dp[-1] = 0

        for i in range(len(nums) - 2, -1, -1):
            for j in range(nums[i]):
                dp[i] = min(dp[i], dp[i + j + 1] + 1) if i + j + 1 < len(nums) else 1
        return dp[0]

