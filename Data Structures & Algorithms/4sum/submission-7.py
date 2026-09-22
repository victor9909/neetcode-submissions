class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        nums.sort()
        res = []

        for i in range(len(nums)):
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            for j in range(i + 1, len(nums)):
                if j > i + 1 and nums[j - 1] == nums[j]:
                    continue
            
                l, r = j + 1, len(nums) - 1
                while l < r:

                    curr_s = nums[i] + nums[j] + nums[l] + nums[r]
                    if curr_s == target:
                        res.append((nums[i], nums[j], nums[l], nums[r]))
                        l += 1
                        while l < len(nums) and nums[l - 1] == nums[l]:
                            l += 1
                    elif curr_s < target:
                        l += 1
                    else:
                        r -= 1
        
        return res