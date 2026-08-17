class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        res = []

        for i, n in enumerate(nums):
            if i > 0 and nums[i-1] == n:
                continue
            
            l, r = i + 1, len(nums) - 1
            while l < r:
                cur_s = n + nums[l] + nums[r]
                if cur_s == 0:
                    res.append((n, nums[l], nums[r]))
                    l += 1
                    while l < len(nums) and nums[l] == nums[l - 1]:
                        l += 1
                elif cur_s > 0:
                    r -= 1
                else:
                    l += 1
        
        return res