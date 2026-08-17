class Solution:
    def rob(self, nums: List[int]) -> int:
        
        cache = {len(nums): 0}

        def dpf(i):
            
            if i in cache:
                return cache[i]

            if i >= len(nums):
                return 0
            
            cache[i] = max(dpf(i+2), dpf(i + 3)) + nums[i]
            return cache[i]
        
        #return max(dpf(0), dpf(1))
        
        dp = [0] * (len(nums) + 3)
        for i in range(len(nums) - 1, -1, -1):
            dp[i] = max(dp[i + 2], dp[i + 3]) + nums[i]
        
        return max(dp[0], dp[1])
        







