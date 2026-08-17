class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        nums_occ = [0] * 3
        for n in nums:
            nums_occ[n] += 1
        
        idx = 0
        for i, c in enumerate(nums_occ):
            for _ in range(c):
                nums[idx] = i
                idx += 1
        
        
        
        