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
        
        return dfs(0)
            

