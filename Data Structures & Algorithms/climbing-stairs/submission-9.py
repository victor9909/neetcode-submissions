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
        if n <= 2:
            return n
        dp_arr = [0] * (n + 1)
        dp_arr[0] = 0
        dp_arr[1] = 1
        dp_arr[2] = 2

        

        for i in range(3, n + 1):
            dp_arr[i] = dp_arr[i - 1] + dp_arr[i - 2]

        return dp_arr[n]