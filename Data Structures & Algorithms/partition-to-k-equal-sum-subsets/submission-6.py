class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        
        target_s = sum(nums)
        if target_s % k != 0:
            return False
        
        target = target_s // k
        nums.sort(reverse=True)

        buckets = [0] * k
        def backtrack(i):
            if i >= len(nums):
                return all(b == target for b in buckets)
            
            for j in range(k):

                if buckets[j] + nums[i] <= target:
                    buckets[j] += nums[i]
                    if backtrack(i + 1):
                        return True
                    buckets[j] -= nums[i]

                if buckets[j] == 0:
                    break
                
            return False
        
        return backtrack(0)