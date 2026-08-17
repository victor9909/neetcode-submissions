class Solution:
    def rob(self, nums: List[int]) -> int:
        
        memo = {}

        def dpf(i: int):

            if i in memo:
                return memo[i]

            if i >= len(nums):
                return 0
            
            memo[i] = max(dpf(i+2), dpf(i+3)) + nums[i]
            return memo[i]
        
        return max(dpf(0), dpf(1))
        