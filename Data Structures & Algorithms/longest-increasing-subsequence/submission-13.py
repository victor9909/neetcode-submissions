class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        memo = {len(nums): 0}

        def dfs(i):
            if i in memo:
                return memo[i]

            if i >= len(nums):
                return 0
            
            res = 0
            for j in range(i + 1, len(nums)):
                if nums[i] >= nums[j]:
                    continue
                res = max(res, dfs(j) + 1)
            memo[i] = res
            return res
        
        res = 0
        for i in range(len(nums)):
            res = max(res, dfs(i) + 1)

        return res
