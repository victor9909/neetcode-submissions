class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        # nums = [1,1,2,3,4], val = 1
        # [2,3,4,1,1]

        idx = 0
        for i, n in enumerate(nums):
            if n != val:
                nums[idx], nums[i] = nums[i], nums[idx]
                idx += 1
        return idx
