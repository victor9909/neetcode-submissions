class Solution:
    def rob(self, nums: List[int]) -> int:
        
        memo = {len(nums): 0}
        
        def backtrack(i):
            if i in memo:
                return memo[i]
            if i >= len(nums):
                return 0
            
            res = nums[i] + max(backtrack(i + 2), backtrack(i + 3))
            memo[i] = res
            return res
        
        #return max(backtrack(0), backtrack(1))

        n = len(nums)
        dp = [0] * (n + 4)
        for i in range(n - 1, -1, -1):
            dp[i] = nums[i] + max(dp[i + 2], dp[i + 3])
        
        return max(dp[0], dp[1])

