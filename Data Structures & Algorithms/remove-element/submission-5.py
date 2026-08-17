class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        if not nums:
            return 0

        
        i, j = 0, 0
        for _ in nums:
            if nums[j] != val:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
            j += 1
        return i


