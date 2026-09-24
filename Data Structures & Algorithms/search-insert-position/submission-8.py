class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        # target 5
        # -1,0,2,4,6,8 l = 0 r = 5 m = 2
        # l = 3 r = 5 m = 4
        # l = 3 r = 3
        

        l, r = 0, len(nums) - 1
        while l <= r:
            m = l + ((r - l) // 2)
            if nums[m] < target:
                l = m + 1
            elif nums[m] > target:
                r = m - 1
            else:
                return m
        
        return l
