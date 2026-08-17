class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = [0] * 3
        for n in nums:
            count[n] += 1
        
        idx = 0
        for i, c in enumerate(count):
            for _ in range(c):
                nums[idx] = i
                idx += 1
        return nums
        