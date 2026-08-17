class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        memo = {}
        def dpf(target: int):
            
            if target == 0:
                return 1
            
            if target in memo:
                return memo[target]

            res = 0
            for n in nums:
                if target - n < 0:
                    continue
                res += dpf(target - n)
            memo[target] = res
            return res
        
        return dpf(target)