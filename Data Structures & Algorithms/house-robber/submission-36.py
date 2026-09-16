class Solution:
    def rob(self, nums: List[int]) -> int:
        
        cache = {len(nums): 0}
        
        def backtrack(i):

            if i in cache:
                return cache[i]

            if i >= len(nums):
                return 0
            
            cache[i] = max(backtrack(i + 2), backtrack(i + 3)) + nums[i]
            return cache[i]
        
        #return max(backtrack(0), backtrack(1))

        n = len(nums)

        if n < 2:
            return max(nums)
        dp = [0] * (n + 1)
        dp[n - 1] = nums[-1]
        dp[n - 2] = nums[-2]
        
        for i in range(n - 3, -1, -1):
            dp[i] = max(dp[i + 2], dp[i + 3]) + nums[i]
        
        return max(dp[0], dp[1])



