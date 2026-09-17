class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        memo = {}

        def dfs(i, curr_s):

            if (i, curr_s) in memo:
                return memo[(i, curr_s)]

            if i >= len(nums):
                return 1 if curr_s == target else 0
            
            memo[(i, curr_s)] = dfs(i + 1, nums[i] + curr_s) + dfs(i + 1, -1 * nums[i] + curr_s)
            return memo[(i, curr_s)]
        
        return dfs(0, 0)
            

            
