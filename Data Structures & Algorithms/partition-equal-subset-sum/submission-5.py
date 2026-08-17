class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        if sum(nums) % 2 != 0:
            return False
        
        target = sum(nums) // 2

        def dfs(idx, curr):

            if curr == target:
                return True
            
            if curr > target or idx >= len(nums):
                return False
            
            return dfs(idx + 1, curr + nums[idx]) or dfs(idx + 1, curr)
        
        return dfs(0, 0)