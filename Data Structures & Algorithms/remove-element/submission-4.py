class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        if not nums:
            return 0

        if nums and len(nums) == 1:
            return 0 if nums[0] == val else 1
        
        # nums = [3,2,2,3] val = 3
        # i = 0, j = 1 [2,3,2,3]
        # i = 1, j = 2 [2,2,3,3]
        # i = 2 j = 3

        # [0,1,2,2,3,0,4,2]
        # i, j = 0, 1 [0,1,2,2,3,0,4,2]
        # i, j = 1, 2 [0,1,2,2,3,0,4,2]
        # i, j = 2, 3 [0,1,2,2,3,0,4,2]

        i, j = 0, 0
        for _ in nums:
            if nums[j] != val:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
            j += 1
        return i


