class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        curr = len(nums)
        for i, n in enumerate(nums):
            curr ^= n ^ i
        
        return curr