class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        sum_nums = sum(nums)
        if sum_nums % 2 != 0:
            return False
        
        cache = {}

        def dfs(idx, curr):
            
            if (idx, curr) in cache:
                return cache[(idx, curr)]

            if curr == sum_nums // 2:
                return True
            
            if idx >= len(nums) or curr > sum_nums:
                return False
            
            cache[(idx, curr)] = dfs(idx + 1,nums[idx] + curr) or dfs(idx + 1,curr)
            return cache[(idx, curr)]
        
        return dfs(0, 0)
