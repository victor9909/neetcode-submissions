class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        res = []
        for i, n in enumerate(nums):

            if i > 0 and nums[i - 1] == n:
                continue
            
            l, r = i + 1, len(nums) - 1
            while l < r:
                curr = nums[l] + nums[r] + n
                if curr == 0:
                    res.append((nums[l],nums[r],n))
                    l += 1
                    while l < len(nums) and nums[l - 1] == nums[l]:
                        l += 1
                elif curr > 0:
                    r -= 1
                else:
                    l += 1
        return res