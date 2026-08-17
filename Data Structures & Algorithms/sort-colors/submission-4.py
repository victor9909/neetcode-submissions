class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = defaultdict(int)
        for n in nums:
            count[n] += 1
        
        idx = 0
        for n in [0, 1, 2]:
            while count[n] > 0:
                nums[idx] = n
                count[n] -= 1
                idx += 1
            