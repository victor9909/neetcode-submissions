class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cnt = Counter(nums)
        res = []
        j = 0
        for i in [0, 1, 2]:
            while i in cnt and cnt[i] > 0:
                cnt[i] -= 1
                nums[j] = i
                j += 1
        
