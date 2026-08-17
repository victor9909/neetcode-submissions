class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        res = []
        for i, n in enumerate(nums):
            if i > 0 and n == nums[i - 1]:
                continue
            
            l, r = i + 1, len(nums) - 1
            while l < r:
                curr_s = n + nums[l] + nums[r]
                if curr_s == 0:
                    res.append([n, nums[l], nums[r]])
                    l += 1
                    while l < len(nums) and nums[l] == nums[l - 1]:
                        l += 1
                elif curr_s > 0:
                    r -= 1
                else:
                    l += 1
        return res
