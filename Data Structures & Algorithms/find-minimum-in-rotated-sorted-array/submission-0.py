class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        # nums = [1,2,3,4,5,6]
        # l = 0, r = 5 -> m = 2 -> 1

        # nums = [3,4,5,6,1,2]
        # l = 0, r = 5 -> m = 2 res = 3
        # l = 3, r = 5 -> m = 4 res = 1
        # l = 5, r = 5 -> m = 5 res = 1

        l, r = 0, len(nums) - 1
        res = float("inf")
        while l <= r:
            m = (l + r) // 2
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            
            res = min(res, nums[m])
            if nums[l] <= nums[m]:
                l = m + 1
            else:
                r = m - 1
        
        return res

