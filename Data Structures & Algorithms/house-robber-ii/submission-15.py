class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]

        def rob_l(nums):

            n = len(nums)
            
            dp = [0] * (n + 4)
            for i in range(n - 1, -1, -1):
                dp[i] = nums[i] + max(dp[i + 2], dp[i + 3])
            
            return max(dp[0], dp[1])
        
        return max(rob_l(nums[1:]), rob_l(nums[:-1]))