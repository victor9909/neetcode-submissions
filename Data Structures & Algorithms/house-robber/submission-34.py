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
        
        return max(backtrack(0), backtrack(1))