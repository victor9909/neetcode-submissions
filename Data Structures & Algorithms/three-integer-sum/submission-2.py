class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        # nums = [-1,0,1,2,-1,-4]
        # [-4, -1, -1, 0, 1, 2]
        # i = 0 l = i + 1 [-4] l+= 1 [-1] r = 5 [2] -3 X
        # i = 0 l = i + 1 [-4] l+= 1  [-1] r = 5 [2] -3 X
        # i = 0 l = i + 1 [-4] l+= 1  [0] r = 5 [2] -2 X
        # i = 0 l = i + 1 [-4] l+= 1  [1] r = 5 [2] -1 X

        # i = 1 l = i  [-1] l += 1  [-1] r = 5 [4] -1 X

        res = []
        nums.sort()
        for idx, n in enumerate(nums):
            if idx > 0 and nums[idx] == nums[idx - 1]:
                continue
        
            l, r = idx + 1, len(nums) - 1
            while l < r:
                curr_sum = nums[l] + nums[r] + n
                if curr_sum == 0:
                    res.append([nums[l], nums[r], n])
                    l += 1
                    while l < len(nums) - 1 and nums[l] == nums[l - 1]:
                        l += 1
                elif curr_sum > 0:
                    r -= 1
                else:
                    l += 1
            
        return res
