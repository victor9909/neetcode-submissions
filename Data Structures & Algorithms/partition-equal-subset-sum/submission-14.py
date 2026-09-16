class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        if sum(nums) % 2:
            return False
        
        target = sum(nums) // 2
        memo = {}

        def backtrack(amount, i):
            if (amount, i) in memo:
                return memo[(amount, i)]

            if amount == 0:
                return True
            
            res = False
            for j in range(i + 1, len(nums)):
                if amount - nums[j] < 0:
                    continue
                res |= backtrack(amount - nums[j], j)
            memo[(amount, i)] = res
            return res
        
        return backtrack(target, 0)
