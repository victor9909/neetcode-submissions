class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        
        arr = [0] * (2 * len(nums))
        for i in range(2 * len(nums)):
            arr[i] = nums[i % len(nums)]
        return arr