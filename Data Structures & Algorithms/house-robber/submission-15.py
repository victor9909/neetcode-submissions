class Solution:
    def rob(self, nums: List[int]) -> int:
        
        memo = {len(nums): 0}
    
        def dp(i):

            if i in memo:
                return memo[i]

            if i >= len(nums):
                return 0
            
            memo[i] = nums[i] + max(dp(i + 2), dp(i + 3))
            return memo[i]
        
        return max(dp(0), dp(1))