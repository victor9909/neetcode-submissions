class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        l, r = 0, len(nums) - 1
        res = float("inf")

        while l <= r:
            
            m = (l + r) // 2
            res = min(nums[m], res)

            if nums[l] <= nums[m]:
                res = min(nums[l], res)
                l = m + 1
            else:
                r = m - 1
        
        return res