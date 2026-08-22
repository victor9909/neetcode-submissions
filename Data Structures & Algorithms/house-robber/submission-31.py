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
        
        return max(dfs(0), dfs(1))