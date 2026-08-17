class Solution:
    def climbStairs(self, n: int) -> int:
        
        memo = {}

        def dp(climbed):

            if climbed in memo:
                return memo[climbed]

            if climbed == n:
                memo[climbed] = 1
                return 1
            
            if climbed > n:
                memo[climbed] = 0
                return 0
            
            memo[climbed] = dp(climbed + 1) + dp(climbed + 2)
            return memo[climbed]
        
        return dp(0)