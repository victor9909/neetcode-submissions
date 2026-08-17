class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        if sum(nums) % 2:
            return False
        
        target = sum(nums) // 2
        memo = {}

        def dpf(i, target):

            if target == 0:
                return True
            
            if (i, target) in memo:
                return memo[(i, target)]

            res = False
            for j in range(i + 1, len(nums)):
                if target - nums[j] < 0:
                    continue
                res |= dpf(j, target - nums[j])
            memo[(i, target)] = res
            return res
        
        return dpf(0, target)
            
