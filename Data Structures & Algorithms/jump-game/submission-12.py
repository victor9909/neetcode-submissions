class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        cache = {}
        def dfs(i):
            
            if i in cache:
                return cache[i]

            if i >= len(nums) - 1:
                return True
            
            res = False
            for j in range(nums[i]):
                res |= dfs(i + j + 1)
            
            cache[i] = res
            return cache[i] 
        
        #return dfs(0)

        dp = [False] * len(nums)
        dp[-1] = True

        for i in range(len(nums) - 2, -1, -1):
            for j in range(nums[i]):
                dp[i] |= dp[i + j + 1] if i + j + 1 < len(nums) else True
        return dp[0]


            

