class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        res = []
        for idx, n in enumerate(nums):
            if idx > 0 and n == nums[idx - 1]:
                continue
            
            l, r = idx + 1, len(nums) - 1
            while l < r:
                three_s = nums[l] + nums[r] + n
                if three_s < 0:
                    l += 1
                elif three_s > 0:
                    r -= 1
                else:
                    res.append([nums[l], nums[r], n])
                    l += 1
                    while l < len(nums) - 1 and nums[l] == nums[l - 1]:
                        l += 1
        return res
