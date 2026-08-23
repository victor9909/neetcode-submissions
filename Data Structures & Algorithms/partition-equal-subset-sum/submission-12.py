class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        if sum(nums) % 2:
            return False
        
        target = sum(nums) // 2
        memo = {}

        def dfs(i, curr_s):
            
            if (i, curr_s) in memo:
                return memo[(i, curr_s)]

            if curr_s == target:
                return True
            if i >= len(nums) and curr_s != target:
                return False
            
            res = False
            for j in range(i + 1, len(nums)):
                if curr_s + nums[j] > target:
                    continue
                res |= dfs(j, curr_s + nums[j])
            memo[(i, curr_s)] = res
            return res
        
        return dfs(0, 0)


