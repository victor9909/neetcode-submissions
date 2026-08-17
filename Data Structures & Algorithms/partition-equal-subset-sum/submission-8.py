class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        if sum(nums) % 2 == 1:
            return False
        
        target = sum(nums) // 2
        memo = {(0, 0): True}

        def dpf(i, target_sum):

            if (i, target_sum) in memo:
                return memo[(i, target_sum)]

            if target_sum == 0:
                return True
            
            res = False
            for j in range(i + 1, len(nums)):
                if target_sum - nums[j] < 0:
                    continue
                res |= dpf(j, target_sum - nums[j])
            memo[(i, target_sum)] = res
            return memo[(i, target_sum)]
        
        return dpf(0, target)
