class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        
        if sum(nums) % k != 0:
            return False
        
        target = sum(nums) // k
        bucket = [0] * k
        nums.sort(reverse=True)

        if nums[0] > target:
            return False

        def backtrack(idx):

            if idx == len(nums):
                return True

            num = nums[idx]
            for i in range(k): 
                if num + bucket[i] > target:
                    continue
                
                bucket[i] += num
                if backtrack(idx + 1):
                    return True

                bucket[i] -= num
                if bucket[i] == 0:
                    break

            return False
        
        return backtrack(0)