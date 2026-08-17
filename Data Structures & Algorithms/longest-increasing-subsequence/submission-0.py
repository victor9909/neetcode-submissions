class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        memo = {}

        def dfs(i):
            LIS = 1
            
            if i in memo:
                return memo[i]

            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    LIS = max(LIS, 1 + dfs(j))
            memo[i] = LIS

            return LIS

        ans = 0
        for i in range(len(nums)):
            ans = max(ans, dfs(i))

        return ans
            

