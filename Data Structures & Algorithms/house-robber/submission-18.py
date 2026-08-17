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
        
        if len(nums) <= 2:
            return max(nums)

        dp_arr = [0] * len(nums)
        dp_arr[0] = nums[0]
        dp_arr[1] = nums[1]
        dp_arr[2] = nums[2] + nums[0]

        for i in range(3, len(nums)):
            dp_arr[i] = nums[i] + max(dp_arr[i - 2], dp_arr[i - 3])
        
        return max(dp_arr[-1], dp_arr[-2])
        