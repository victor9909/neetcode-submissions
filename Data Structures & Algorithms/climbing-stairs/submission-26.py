class Solution:
    def climbStairs(self, n: int) -> int:
        
        memo = {n: 1}

        def backtrack(i):

            if i in memo:
                return memo[i]

            if i == n:
                return 1
            if i > n:
                return 0

            memo[i] = backtrack(i + 1) + backtrack(i + 2)
            return memo[i]
        
        #return backtrack(0)

        if n <= 2:
            return n

        step1, step2 = 1, 2
        for i in range(3, n + 1):
            tmp1, tmp2 = step1, step2
            step1 = tmp2
            step2 = tmp1 + tmp2

        return step2




