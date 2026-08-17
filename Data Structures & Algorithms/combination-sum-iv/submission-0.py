class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        memo = {}
        def dpf(i: int, target: int):
            
            if target == 0:
                return 1
            
            if (i, target) in memo:
                return memo[(i, target)]

            res = 0
            for j in range(i, len(nums)):
                if target - nums[j] < 0:
                    continue
                res += dpf(i, target - nums[j])
            memo[(i, target)] = res
            return res
        
        return dpf(0, target)