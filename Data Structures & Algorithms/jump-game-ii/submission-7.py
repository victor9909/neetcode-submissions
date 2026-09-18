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
        
        return dfs(0)