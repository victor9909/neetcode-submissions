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
        
        return max(backtrack(0), backtrack(1))