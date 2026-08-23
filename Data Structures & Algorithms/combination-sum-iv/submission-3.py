class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        memo = {}

        def dfs(target):
            
            if target in memo:
                return memo[target]

            if target == 0:
                return 1
            
            res = 0
            for n in nums:
                if target - n < 0:
                    continue
                res += dfs(target - n)
            memo[target]  = res
            return res
        
        return dfs(target)