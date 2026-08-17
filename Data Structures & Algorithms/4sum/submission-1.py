class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        nums.sort()
        res = []

        for i, n in enumerate(nums):
            if i > 0 and nums[i - 1] == n:
                continue
            
            for j in range(i+1, len(nums)):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                l, r = j + 1, len(nums) - 1
                while l < r:
                    curr_s = n + nums[j] + nums[l] + nums[r]
                    if curr_s < target:
                        l += 1
                    elif curr_s > target:
                        r -= 1
                    else:
                        res.append((n, nums[j], nums[l], nums[r]))
                        l += 1
                        while l < len(nums) - 1 and nums[l] == nums[l - 1]:
                            l += 1
        return res